#!/bin/bash
#script that takes in a URL, sends a request to that URL
#and displays the size of the body of the moessage
curl -sI "$1" | awk '/Content-Length/{print $2}'
