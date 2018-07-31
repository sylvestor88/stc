"""
__author__ = "Sylvestor George"
__version__ = "1.0"
__maintainer__ = "Sylvestor George"
__email__ = "sylvestor.george88@gmail.com"
"""

from flask import Blueprint, jsonify, request, make_response

events = Blueprint('events', __name__)


@events.route('')
def index():
    return make_response(
        jsonify(message='Judy Platform Orchestration Services are Running.'),
        200)
