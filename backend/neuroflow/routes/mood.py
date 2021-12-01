"""
Author: Isamu Isozaki (isamu.website@gmail.com)
Description: description
Created:  2021-12-01T16:32:53.089Z
Modified: !date!
Modified By: modifier
"""

from flask import Blueprint, redirect, jsonify, url_for, request


blueprint = Blueprint('mood', __name__, 
                            url_prefix='/mood')

@blueprint.route('/mood', methods=['POST'])
def mood_processing():
    """
    """
    try:
        request_json = request.get_json()
        mood = float(request_json['mood'])
    except:
        return "Invalid request.", 400
    
    return jsonify({'status': 'OK'})