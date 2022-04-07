# Console App

import requests
import uuid
from datetime import datetime, timedelta, date
import random

def generateUUID():
    return uuid.uuid4().hex

# This app contains functionality for local development

# Grind Log API Endpoints
grind_log_api = 'http://localhost:5001'
create_default_user_profile_endpoint = grind_log_api + '/create-default-user-profile'
retrieve_user_profile_endpoint = grind_log_api + '/retrieve-user-profile'
create_check_in_record_endpoint = grind_log_api + '/create-check-in-record'

# ----------------------------------------------------------------------------------------------------
# User Profiles
# ----------------------------------------------------------------------------------------------------
def createDefaultUserProfile():
    requests.get(create_default_user_profile_endpoint)

def retrieveDefaultUserProfile():
    # Create the default user profile
    createDefaultUserProfile()
    # The default user id is '1'
    user_id = '1'
    # Load it into the params
    params = {"user_id": user_id}
    # Make the request
    default_user_profile = requests.get(retrieve_user_profile_endpoint, params=params)
    # Return it
    return default_user_profile

# ----------------------------------------------------------------------------------------------------
# Sessions
# ----------------------------------------------------------------------------------------------------

def newSession():
    pass

# ----------------------------------------------------------------------------------------------------
# Mock Data
# ----------------------------------------------------------------------------------------------------

def generateRandomQuestion():
    questions = ["How are you?",
                 "Whats up?",
                 "What's new?"]
    return random.choice(questions)

def generateRandomAnswer():
    answers = ["The sky is green",
               "You are awesome",
               "I love Anna"]
    return random.choice(answers)

def generateRandomCheckInDataForDate(date):
    # Define how many questions and answers will be generated
    question_answer_count = 5
    # Generate the Session ID
    check_in_id = generateUUID()
    # Set the question index to 0
    question_index = 0
    # Set the date
    check_in_date = date
    # Generate a list of questions
    questions = []
    for i in range(question_answer_count):
        question = generateRandomQuestion()
        questions.append(question)
    # Generate a list of answers
    answers = []
    for i in range(question_answer_count):
        answer = generateRandomAnswer()
        answers.append(answer)
    # Create the map representation of it
    map_rep = {"check_in_id": check_in_id,
               "question_index": question_index,
               "date": check_in_date,
               "questions": questions,
               "answers": answers}
    return map_rep

def generateMockDataForToday(dataList):
    # Define how many check ins will be generated for today
    check_in_count = 3
    # Get todays date
    today = date.today()
    # Midnight tonight
    midnightTonight = datetime.combine(today, datetime.min.time()) + timedelta(minutes=1439)
    # Generate range of dates in the day
    minutesInADay = 1440
    dates = []
    for i in range(check_in_count):
        # Generate a random minute to subtract from midnight
        r = random.randint(1, 1439)
        randDate = midnightTonight - timedelta(minutes=r)
        dates.append(randDate)
    # Generate random check in data for the generated dates and
    # add it to the dataList reference
    for d in dates:
        randomDataForDate = generateRandomCheckInDataForDate(d)
        dataList.append(randomDataForDate)

def generateMockDataForLastWeek(dataList):
    # Define how many check ins will be geneerated for last week
    check_in_count = 14
    # Get todays date
    today = date.today()
    # Midnight tonight
    midnightTonight = datetime.combine(today, datetime.min.time()) + timedelta(minutes=1439)
    # Generate a range of dates in the last week
    minutesInAWeek = 10080
    dates = []
    for i in range(check_in_count):
        # Generate a random minute to subtract
        r = random.randint(1, 10079)
        randDate = midnightTonight - timedelta(minutes=r)
        dates.append(randDate)
    # Generate random check in data for the generated dates and
    # add it to the dataList reference
    for d in dates:
        randomDataForDate = generateRandomCheckInDataForDate(d)
        dataList.append(randomDataForDate)

def generateMockDataForLastMonth(dataList):
    # Define how many check ins will be generated for last week
    check_in_count = 30
    # Get todays date
    today = date.today()
    # Midnight tonight
    midnightTonight = datetime.combine(today, datetime.min.time()) + timedelta(minutes=1439)
    # Genterate a range of dates in the last month
    minutesInAMonth = 43800
    dates = []
    for i in range(check_in_count):
        # Generate a random minute to subtract
        r = random.randint(1, 43799)
        randDate = midnightTonight - timedelta(minutes=r)
        dates.append(randDate)
    # Generate random check in data for the generated dates and
    # add it to the dataList reference
    for d in dates:
        randomDataForDate = generateRandomCheckInDataForDate(d)
        dataList.append(randomDataForDate)

def generateMockDataForLastYear(dataList):
    # Define how many check ins will be generated for the last year
    check_in_count = 100
    # Get todays date
    today = date.today()
    # Midnight tonight
    midnightTonight = datetime.combine(today, datetime.min.time()) + timedelta(minutes=1439)
    # Generate a range of dates in the last year
    minutesInAYear = 525600
    dates = []
    for i in range(check_in_count):
        # Generate a random minute to subtract
        r = random.randint(1, 525599)
        randDate = midnightTonight - timedelta(minutes=r)
        dates.append(randDate)
    # Generate random check in data for the generated dates and
    # add it to the dataList reference
    for d in dates:
        randomDataForDate = generateRandomCheckInDataForDate(d)
        dataList.append(randomDataForDate)

def generateMockData():
    # Generate the prompt
    prompt = "\nGenerating Mock Check In Data...\n\n"
    prompt += "What would you like to do?\n"
    prompt += "  1. Generate a lot of data (default)\n"
    prompt += "  2. Generate data for today\n"
    prompt += "  3. Generate data for the last week\n"
    prompt += "  4. Generate data for the last month\n"
    prompt += "  5. Generate data for the last year\n"
    selection = input(prompt)

    # Define a list that will contain the generated check ins
    dataList = []

    if selection == "2":
        generateMockDataForToday(dataList)
    elif selection == "3":
        generateMockDataForLastWeek(dataList)
    elif selection == "4":
        generateMockDataForLastMonth(dataList)
    elif selection == "5":
        generateMockDataForLastYear(dataList)
    else:
        generateMockDataForToday(dataList)
        generateMockDataForLastWeek(dataList)
        generateMockDataForLastMonth(dataList)
        generateMockDataForLastYear(dataList)

    # Create each check in on the server
    for checkInData in dataList:
        requests.post(create_check_in_record_endpoint, params=checkInData)

# ----------------------------------------------------------------------------------------------------

prompt = "What would you like to do?\n"
prompt += "1. Create Session\n"
prompt += "2. Mock Test Data\n"
selection = input(prompt)

if selection == "1":
    newSession()
if selection == "2":
    generateMockData()