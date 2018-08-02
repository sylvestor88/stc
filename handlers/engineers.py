"""
__author__ = "Sylvestor George"
__version__ = "1.0"
__maintainer__ = "Sylvestor George"
__email__ = "sylvestor.george88@gmail.com"
"""

from flask import Blueprint, jsonify, request, make_response
from models.Deployments import Deployments
from db.sqlite import db_session

engineers = Blueprint('engineers', __name__)


@engineers.route('/list')
def get_distinct_engineers():
    """
    GET list of Engineers
    ---
    tags:
      - Slack Technical Challenge
    responses:
      200:
        description: List of Engineers
      404:
        description: No Engineers Found
      500:
        description: Server Error while executing request
    """
    # Queries DB for list of Engineers
    distinct_engineers = db_session.query(Deployments.engineer).distinct().\
        order_by(Deployments.engineer)
    if distinct_engineers.count() > 0:
        list_of_engineers = list()
        for engineer in distinct_engineers:
            list_of_engineers.append(engineer.engineer)

        return make_response(jsonify(
            listOfEngineers=list_of_engineers,
            totalEngineers=len(list_of_engineers)),
            200)
    else:
        return make_response(jsonify(error='No Engineers Found.'),
                             404)
