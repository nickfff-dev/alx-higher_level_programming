#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to
the URL and displays the body of the response
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        print(response.text)
    except requests.exceptions.HTTPError as e:
        if e.status_code >= 400:
            print("Error code: {}".format(e.status_code))
