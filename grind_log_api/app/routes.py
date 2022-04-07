from flask import jsonify, make_response, request, json, g
import dateutil.parser
import datetime
import json
import uuid
import requests

from app import app
from app import api as api

def generateUUID():
    return uuid.uuid4().hex

@app.route('/create-default-user-profile', methods=['GET', 'POST'])
def createDefaultUserProfile():
    # Create the default user id
    user_id = '1'
    # The default user profile email is my email
    email = 'jnelsen788@gmail.com'
    # The Default User Profile Check In Time is now
    check_in_time = datetime.datetime.now().isoformat()
    # Create the default user profile
    api.persistUserProfile(user_id, email, check_in_time)
    # Form the response body
    response_body = {
        "success": 0
    }
    return make_response(jsonify(response_body), 200)

@app.route('/retrieve-user-profile', methods=['GET', 'POST'])
def retrieveUserProfile():
    # Get the user id from the request
    user_id = request.args.get('user_id')
    # Retrieve the JSON from the database
    response_body = api.getUserProfile(user_id)
    # Return the response
    return make_response(jsonify(response_body), 200)

@app.route('/create-check-in-record', methods=['GET', 'POST'])
def createCheckInRecord():
    # Name the check in
    check_in_args = request.args
    # Check In already in map form so send directly to the API
    api.persistCheckIn(check_in_args)
    # Form the response body
    response_body = {
        "success": 0
    }
    return make_response(jsonify(response_body), 200)

@app.route('/retrieve-todays-checkins', methods=['GET','POST'])
def retrieveTodaysCheckIns():
    # Get todays date from the request
    currentTimeISO = request.args.get('date')
    # Retrieve today's check ins
    checkins = api.getTodaysCheckIns(currentTimeISO)
    # Form the response body
    response_body = {
        "check-ins": checkins
    }
    return make_response(jsonify(response_body), 200)