#!/bin/bash

# Start the local Firebase emulator

# Kill Auth port
fuser -k 9099/tcp
# Kill Functions port
fuser -k 9098/tcp
# Kill Firestore port
fuser -k 9097/tcp
# Kill Database port
fuser -k 9096/tcp
# Kill Hosting port
fuser -k 9095/tcp
# Kill pubsub port
fuser -k 9094/tcp
# Kill UI port
fuser -k 9090/tcp

# Start the local Firebase services
echo 'Starting Firebase Local Emulator server...'
gnome-terminal -e 'sh -c "echo ''Firebase Local Emulator server...''; firebase emulators:start;"'