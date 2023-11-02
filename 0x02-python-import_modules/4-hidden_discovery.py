#!/usr/bin/python3
import hidden_4


def print_names():

    for name in dir(hidden_4):
        if name[0] == '_' and name[1] == '_':
            continue
        print(name)


if __name__ == "__main__":
    print_names()
