#!/usr/bin/python3
"""
    Module implementing a script that takes a letter, sends
    a POST request to the given url with the letter as
    parameter
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv[1]) == 1:
        q = ""
    else:
        q = sys.argv[1]

    payload = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'

    try:
        response = requests.post(url, data=payload)
        data = response.json()

        if data:
            print(f"[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
