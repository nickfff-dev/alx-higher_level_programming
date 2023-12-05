#!/bin/bash
# This script sends a GET request to a URL and displays the body of a 200 status code response
curl -sL -w "%{http_code}" "$1" | grep -v "200" || echo
