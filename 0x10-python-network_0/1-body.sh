#!/bin/bash
# takes url, sends GET request to the url, returns body of the response
curl -s "$1" | grep -iE "^HTTP/.* 200" && curl -s "$1"
