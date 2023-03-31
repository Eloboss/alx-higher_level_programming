#!/bin/bash
#script that takes in a URL and display size of the message body
curl -sI "$1" | grep -E 'Content-Length: [0-9]+' | cut -d ":" -f2

