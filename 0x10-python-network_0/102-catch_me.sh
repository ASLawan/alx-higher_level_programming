#!/bin/bash
# make a request to 0.0.0.0:5000/catch_me that causes server responds
curl -s -L 0.0.0.0:5000/catch_me -X PUT -H "Origin: HolbertonSchool"
