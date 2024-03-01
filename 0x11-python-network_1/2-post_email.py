#!/usr/bin/python3
"""
    Module implementing a script to take a url,
    send a POST request, with email as parameter
    and displays the body of the response
"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({'email': email})
    data = data.encode('ascii')

    with request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')
        print(body)
