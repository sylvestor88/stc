"""
__author__ = "Sylvestor George"
__version__ = "1.0"
__maintainer__ = "Sylvestor George"
__email__ = "sylvestor.george88@gmail.com"
"""
import time
import datetime
import collections
from flask import Blueprint, jsonify, request, make_response
from sqlalchemy import and_, desc
from models.Deployments import Deployments
from db.sqlite import db_session

events = Blueprint('events', __name__)


@events.route('')
def get_events():
    """
    GET list of event or events summary for given datetime range
    ---
    tags:
      - Slack Technical Challenge
    parameters:
      - in: query
        name: start_range
        schema:
            type: integer
        description: Start time range to search for events
      - in: query
        name: end_range
        schema:
            type: integer
        description: End time to range search for events
      - in: query
        name: group_by_day
        schema:
            type: boolean
        description: To Group events summary by day
    responses:
      200:
        description: Events Details/Events Statistics
      404:
        description: No Engineers Found
      500:
        description: Server Error while executing request
    """
    # request parameters
    since = request.args.get('start_range', 0)
    end = request.args.get('end_range', int(time.time()))
    group_by_day = request.args.get('group_by_day', False)

    # Queries for Events in given time range
    events_result = db_session.query(Deployments).filter(
        and_(Deployments.date >= since, Deployments.date <= end)).order_by(desc(Deployments.date))

    # Checks for events retrieved from DB
    if events_result.count() <= 0:
        return make_response(jsonify(error='No Events Found.'), 404)
    else:
        if group_by_day:
            daily_summary = events_summary(events_result)
            return make_response(jsonify(summary=daily_summary,
                                         totalEvents=events_result.count()), 200)

        else:
            list_of_events = list()
            for event in events_result:
                list_of_events.append(event.model_obj_as_dict())

            return make_response(jsonify(events=list_of_events,
                                         totalEvents=len(list_of_events)), 200)


def events_summary(events_results):
    """
    Aggregates Events Summary

    :param      events_results: list of events from DB
    :type       events_results: list
    :return:    summary:        Daily events statistics
    :rtype:     summary:        dict
    """
    # Events Summary
    summary = collections.OrderedDict()

    for event in events_results:
        # Gets the day of the event
        event_date = datetime.datetime.fromtimestamp(event.date).strftime('%Y-%m-%d')
        # Event Action
        action = event.action

        # Check if events date exists in summary data
        if event_date not in summary:
            date_statistics = {action: 1}
            summary[event_date] = date_statistics
        else:
            # Adds action type if exists
            if action not in summary[event_date]:
                summary[event_date][action] = 1
            else:
                # Increments by 1 if action already exists
                summary[event_date][action] += 1

    return summary
