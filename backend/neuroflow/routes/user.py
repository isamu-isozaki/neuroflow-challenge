"""
Author: Isamu Isozaki (isamu.website@gmail.com)
Description: description
Created:  2021-12-01T16:32:53.089Z
Modified: !date!
Modified By: modifier
"""

from flask import Blueprint, redirect, jsonify, url_for, request
from neuroflow.repository import create_user, load_user_from_email, save_token
import os
import binascii


blueprint = Blueprint('user', __name__, 
                            url_prefix='/')

@blueprint.route('/get_token', methods=['POST'])
def get_token():
    try:
        request_json = request.get_json()
        email = request_json['email']
        password = request_json['password']
    except:
        return "Invalid request. Send a POST request with valid payload or check the documentation", 400
    user = load_user_from_email(email)
    if not user or not user.check_password(password):
        return "Invalid credentials", 401
    token = save_token({
        'access_token': binascii.b2a_hex(os.urandom(100)).decode('utf-8'),
        'refresh_token': binascii.b2a_hex(os.urandom(100)).decode('utf-8'),
        'user_id': user.id
    })

    return jsonify({'token': token.access_token})


@blueprint.route('/create', methods=['POST'])
def post_user():
    try:
        request_json = request.get_json()
        email = request_json['email']
        first_name = request_json['first_name']
        last_name = request_json['last_name']
        password = request_json['password']
    except:
        return "Invalid request. Send a GET request with valid payload or check the documentation", 400
    if not create_user(email, first_name, last_name, password):
        return "User already made", 400
    
    return 'Success', 200