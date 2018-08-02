"""
__author__ = "Sylvestor George"
__version__ = "1.0"
__maintainer__ = "Sylvestor George"
__email__ = "sylvestor.george88@gmail.com"
"""

from flask import Blueprint, jsonify, make_response
from models.Deployments import Deployments
from db.sqlite import db_session

engineers = Blueprint('engineers', __name__)


@engineers.route('')
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


@engineers.route('<string:eng_id>/events')
def get_events_by_engineer(eng_id):
    """
    GET events performed by an Engineer
    ---
    tags:
      - Slack Technical Challenge
    parameters:
      - in: path
        name: eng_id
        schema:
            type: string
        required: true
        description: Engineers ID
    responses:
      200:
        description: List of Events by an Engineer
      404:
        description: No Events found by an Engineer
      500:
        description: Server Error while executing request
    """
    # Queries DB for events by Engineers name
    events_by_engineer = db_session.query(Deployments).filter(
        Deployments.engineer == eng_id)

    if events_by_engineer.count():
        list_of_events = list()
        for event in events_by_engineer:
            list_of_events.append(event.model_obj_as_dict())

        return make_response(jsonify(events=list_of_events,
                                     totalEvents=len(list_of_events)), 200)
    else:
        return make_response(jsonify(error='No Events Found for engineer: {0}'.format(eng_id)), 404)
