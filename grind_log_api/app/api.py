import json
import requests
import uuid
from datetime import datetime, timedelta, date
from dateutil import parser

from app import db

def generateUUID():
    return uuid.uuid4().hex

def persistUserProfile(user_id, email, check_in_time):
    # Create the document
    user_profile = {'user_id': user_id,
                    'email': email,
                    'check_in_time': check_in_time}
    # Get the document reference
    ref = db.collection('user_profile').document(user_id)
    # Set the document
    ref.set(user_profile)

def getUserProfile(user_id):
    pass

def persistQuestions(check_in_id, check_in):
    # Get the collection
    coll = db.collection('question')
    # Save each question
    questions = check_in.getlist('questions')
    for i in range(len(questions)):
        data = {'check_in_id': check_in_id,
                'check_in_question_index': i,
                'question': questions[i]}
        ref = coll.document(generateUUID())
        ref.set(data)

def persistAnswers(check_in_id, check_in):
    # Get the collection
    coll = db.collection('answer')
    # Save each question
    answers = check_in.getlist('answers')
    for i in range(len(answers)):
        data = {'check_in_id': check_in_id,
                'check_in_answer_index': i,
                'answer': answers[i]}
        ref = coll.document(generateUUID())
        ref.set(data)


def persistCheckIn(check_in):
    # Get the check in ID
    check_in_id = check_in.get('check_in_id')
    # Persist the questions
    persistQuestions(check_in_id, check_in)
    # Persist the answers
    persistAnswers(check_in_id, check_in)
    # Get the document reference
    ref = db.collection('check_in').document(check_in_id)
    # Set the document
    ref.set(check_in)

def retrieveQuestionsAndAnswers(checkIns):
    updatedCheckIns = []
    # For each Check In Dict
    for c in checkIns:
        # Get the Check In Id
        check_in_id = c['check_in_id']

        # Get the Questions collection
        coll = db.collection('question')
        # Form the query
        query = coll.where('check_in_id', '==', check_in_id)
        # Execute the query
        results = query.get()
        # Collect the Questions
        questions = []
        for r in results:
            questions.append(r.to_dict()['question'])
        # Set the questions on the Check In Dict
        c['questions'] = questions

        # Get the Answers collection
        coll = db.collection('answer')
        # Form the query
        query = coll.where('check_in_id', '==', check_in_id)
        # Execute the query
        results = query.get()
        # Collect the Answers
        answers = []
        for r in results:
            answers.append(r.to_dict()['answer'])
        # Set the answers on the Check In Dict
        c['answers'] = answers

        # Add the Check In the the Accumulator
        updatedCheckIns.append(c)
    # Return the updated check ins
    return updatedCheckIns

def getTodaysCheckIns(currentTimeISO):
    # Convert the current time sent by the app to a datetime
    currentDateTime = parser.parse(currentTimeISO)
    # Set the beginning of the range
    midnightThisMorning = datetime.combine(currentDateTime, datetime.min.time())
    # Set the end of the range
    midnightTonight = midnightThisMorning + timedelta(minutes=1439)
    # Retrieve the db collection
    ref = db.collection('check_in')
    # Form the query
    query = ref.where('date', '>=', midnightThisMorning)
    query = query.where('date', '<=', midnightTonight)
    # Get the results
    dbResults = ref.get()
    # Convert to list of dicts
    checkInResults = []
    for r in dbResults:
        checkInResults.append(r.to_dict())
    # Set the questions and answers on the check ins
    checkInResults = retrieveQuestionsAndAnswers(checkInResults)
    # Return the results
    return checkInResults