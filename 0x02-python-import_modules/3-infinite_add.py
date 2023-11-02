#!/usr/bin/python3
import sys


def infinite_add():

    args = sys.argv
    num_args = len(args)
    sum = 0
    for i in range(1, num_args):
        sum += int(args[i])
    print(sum)


if __name__ == "__main__":
    infinite_add()
