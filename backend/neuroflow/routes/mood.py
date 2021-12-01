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