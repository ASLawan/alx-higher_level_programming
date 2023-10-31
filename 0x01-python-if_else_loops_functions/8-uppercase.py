#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            upper += chr(ord(s) - 32)
        else:
            upper += s
    print("{}".format(upper))
