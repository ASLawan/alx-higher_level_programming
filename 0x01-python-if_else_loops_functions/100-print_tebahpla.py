#!/usr/bin/python3
for c in "zyxwvutsrqponmlkjihgfedcba":
    result = ""
    if ord(c) % 2 == 1:
        result += chr(ord(c) - 32)
    else:
        result += c
    print("{}".format(result), end="")
