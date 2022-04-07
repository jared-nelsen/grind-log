# Grind Log
  - Jared Nelsen Sept 1, 2021
-------------------------------------------------------------------------------------------------------------------------------------

The AI Powered Work Journal

-------------------------------------------------------------------------------------------------------------------------------------

# Game Plan

    - Sessions
    - User Profiles
        - Email
        - Check In Time
    - Heartbeat Service

-------------------------------------------------------------------------------------------------------------------------------------

# Architecture

  The Units of Lustro are:

    - Grind Log Interviewer
        - The Flutter App that carries out the interview
    - Grind Log API
        - The central API that manages interviews, interview plans, and the administration of interviews
    - Notification Generator
        - Creates Sessions and sends notifications about Interviews

# Ports

    - Grind Log Interviewer: 5555
    - Grind Log API: 5001

    - Auth emulator - 9099
    - Functions emulator - 9098
    - Firestore emulator -9097
    - Database emulator - 9096
    - Hosting emulator - 9095
    - Pubsub emulator - 9094
    - Emulator UI - 9090

-------------------------------------------------------------------------------------------------------------------------------------

# Links

## Flutter

    - Dockerizing Flutter apps: https://blog.codemagic.io/how-to-dockerize-flutter-apps/
    - Video detailing Flutter web release strategies (Dart Web servers): https://www.youtube.com/watch?v=yoAdPgw7YLM

## Kubernetes

    - Developing services locally: https://cloud.google.com/community/tutorials/developing-services-with-k8s
    
## Docker

    - Install Docker on Linux Mint: https://computingforgeeks.com/install-docker-and-docker-compose-on-linux-mint-19/
    - User Permission Denied Fix: https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue

## Dart

    - Simple Dart http servers: https://dart.dev/tutorials/server/httpserver

## Flask

    - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
    
## Firestore

    - Install FireStore https://firebase.google.com/docs/cli#install-cli-mac-linux
    - Install Local Emulator Suite - https://firebase.google.com/docs/emulator-suite/install_and_configure
    - Use Python for local database - https://stackoverflow.com/questions/54868011/how-to-use-google-cloud-firestore-local-emulator-for-python-and-for-testing-purp
    - Start local emulator
        - firebase emulators:start
        - Hosted on port 4000
    - Firestore and Flask - https://gaedevs.com/blog/how-to-use-the-firestore-emulator-with-a-python-3-flask-app

## Kubernetes

   - Logging: https://logz.io/blog/a-practical-guide-to-kubernetes-logging/
   - Install Minikube: https://phoenixnap.com/kb/install-minikube-on-ubuntu

-------------------------------------------------------------------------------------------------------------------------------------

# Development Environment Setup

   - TODO

-------------------------------------------------------------------------------------------------------------------------------------
## A note on question types

Ideally an interview is an organic experience with different types of questions. This is something I can emulate.

Types of questions:

1. Dichotomous Yes or No questions
2. Elaborative questions
3. Multiple Choice Questions
4. Text Slider Questions
5. Open Ended Questions
6. Thumbs Up Thumbs Down Question
7. User entered question