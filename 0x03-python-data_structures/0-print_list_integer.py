#!/usr/bin/python3

def print_list_integer(my_list=[]):

    num = len(my_list)
    i = 0
    while i < num:
        print("{:d}".format(my_list[i]))
        i += 1


if __name__ == "__main__":
    print_list_integer(my_list=[])
