#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if 10 - j == 1 and 10 - i == 2:
            print("{}{}".format(i, j))
            break
        print("{}{}, ".format(i, j), end="")
