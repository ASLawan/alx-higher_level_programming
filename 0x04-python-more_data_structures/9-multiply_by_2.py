#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    new_dict = {}
    for k, v in a_dictionary.items():
        new_dict[k] = v * 2

    return new_dict


if __name__ == "__main__":
    multiply_by_2(a_dictionary)
