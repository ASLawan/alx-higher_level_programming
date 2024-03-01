#!/usr/bin/python3
"""
    Module to implement a script that takes a url, and an email
    sends a POST request to the url with email as parameter

"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)
