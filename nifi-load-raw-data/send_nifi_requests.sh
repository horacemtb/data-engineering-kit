#!/bin/bash

# Check if the number of requests is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <number_of_requests>"
  exit 1
fi

# Number of requests to send (provided as a parameter)
NUM_REQUESTS=$1

# URL to send requests to
URL="http://127.0.0.1:8081/loglistener"

# Loop to send requests of the first type
for i in $(seq 1 $NUM_REQUESTS); do
  # Generate a unique string for each request
  UNIQUE_TEXT="adbrsgbndt ERROR fevrtb $i"
  
  # Send the request
  curl --data "$UNIQUE_TEXT" $URL
  
  # Optional: Add a small delay between requests to avoid overwhelming the server
  sleep 0.1
done

# Loop to send requests of the second type
for i in $(seq 1 $NUM_REQUESTS); do
  # Generate a unique string for each request
  UNIQUE_TEXT="uiebveovne $i"
  
  # Send the request
  curl --data "$UNIQUE_TEXT" $URL
  
  # Optional: Add a small delay between requests to avoid overwhelming the server
  sleep 0.1
done