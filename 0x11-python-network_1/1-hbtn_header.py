#!/usr/bin/python3
"""
    Module implementing a script that takes a url
    sends a request to the url and displays the value
    of the X-Request-Id
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
