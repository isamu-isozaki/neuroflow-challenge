"""
Author: Isamu Isozaki (isamu.website@gmail.com)
Description: description
Created:  2021-12-01T16:32:53.089Z
Modified: !date!
Modified By: modifier
"""

from flask import Blueprint, redirect, jsonify, url_for, request
from neuroflow.repository import create_mood, get_authorized
from functools import wraps
from flask_cors import cross_origin

blueprint = Blueprint('mood', __name__, 
                            url_prefix='/mood')

def authorized():
    def authorized_decorator(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if not request.headers.get('Authorization', None):
                return 'Unauthorized', 401
            user = get_authorized(request)
            print(user)
            if not user:
                return 'Unauthorized', 401
            return f(user, *args, **kwargs)
    
        return wrap
    return authorized_decorator

@blueprint.route('', methods=['POST'])
@cross_origin()
@authorized()
def mood_processing(user):
    try:
        request_json = request.get_json()
        mood_val = float(request_json['mood'])
        assert 0 <= mood_val <= 10
        mood = create_mood(mood_val, user)
    except Exception as e:
        print(e)
        return "Invalid request.", 400
    print(mood)
    del mood['_sa_instance_state']
    del mood['user']
    return jsonify({'mood': mood})