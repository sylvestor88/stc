"""
__author__ = "Sylvestor George"
__version__ = "1.0"
__maintainer__ = "Sylvestor George"
__email__ = "sylvestor.george88@gmail.com"
"""
import datetime
from flask import Blueprint, jsonify, make_response
from sqlalchemy import and_
from models.Deployments import Deployments
from db.sqlite import db_session

events = Blueprint('events', __name__)


@events.route('/time-range/<int:begin>/to/<int:end>')
def get_events_by_time_range(begin, end):
    """
    GET events within time range
    ---
    tags:
      - Slack Technical Challenge
    parameters:
      - in: path
        name: begin
        type: string
        required: true
      - in: path
        name: end
        type: string
        required: true
    responses:
      200:
        description: List of Events for given time range
      404:
        description: No Engineers Found for given time range
      500:
        description: Server Error while executing request
    """

    # Queries DB for events by date range
    events_by_range = db_session.query(Deployments).filter(
        and_(Deployments.date >= begin, Deployments.date <= end))

    if events_by_range.count() > 0:
        list_of_events = list()
        for event in events_by_range:
            list_of_events.append(event.model_obj_as_dict())

        return make_response(jsonify(events=list_of_events,
                                     totalEvents=len(list_of_events)), 200)
    else:
        return make_response(jsonify(error='No Events Found for range {0} to '
                                           '{1}'.format(begin, end)), 404)


@events.route('/engineer/<string:name>')
def get_events_by_engineer(name):
    """
    GET events by an Engineer
    ---
    tags:
      - Slack Technical Challenge
    parameters:
      - in: path
        name: name
        type: string
        required: true
    responses:
      200:
        description: List of Events by an Engineer
      404:
        description: No Events found by an Engineer
      500:
        description: Server Error while executing request
    """
    # Queries DB for events by Engineers name
    events_by_engineer = db_session.query(Deployments).filter(Deployments.engineer==name)

    if events_by_engineer.count():
        list_of_events = list()
        for event in events_by_engineer:
            list_of_events.append(event.model_obj_as_dict())

        return make_response(jsonify(events=list_of_events,
                                     totalEvents=len(list_of_events)), 200)
    else:
        return make_response(jsonify(error='No Events Found for user: '
                                           '{0}'.format(name)), 404)


@events.route('/daily-summary')
def get_events_summary():
    """
    GET events summary by day
    ---
    tags:
      - Slack Technical Challenge
    responses:
      200:
        description: Events Summary by day
      404:
        description: No Events found.
      500:
        description: Server Error while executing request
    """
    group_by_action = db_session.query(Deployments.date).group_by(Deployments.action).all()

    if group_by_action:
        print(group_by_action)
        return make_response(jsonify(error='No Events Found!'), 200)
        # events_summary = dict()
        # for event in list_of_events:
        #     event_date = datetime.datetime.fromtimestamp(event.date).strftime('%Y-%m-%d')
        #     if event_date in events_summary:
        #         pass
        #     else:
        #         events_summary[]
    else:
        return make_response(jsonify(error='No Events Found!'), 404)

    # events_by_range = db_session.query(Deployments).filter(
    #     and_(Deployments.date >= begin, Deployments.date <= end))
    #
    # if events_by_range:
    #     events = list()
    #     for event in events_by_range:
    #         events.append(event.model_obj_as_dict())
    #
    #     return make_response(jsonify(events=events), 200)
    # else:
    #     return make_response(jsonify(error='No Events Found for range ' + begin + " to " + end), 404)
