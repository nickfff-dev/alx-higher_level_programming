#!/bin/bash
# This script sends a request to a URL and displays the size of the body of the response
url=$1
curl -sI "$url" | grep 'Content-Length' | cut -d' ' -f2
