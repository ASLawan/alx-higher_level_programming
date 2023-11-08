#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    for k in sorted(a_dictionary.keys()):
        v = a_dictionary[k]
        print("{}: {}".format(k, v))


if __name__ == "__main__":
    print_sorted_dictionary(a_dictionary)
