#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    length = len(my_list) - 1
    my_list_cpy = my_list[:]
    if idx < 0:
        return my_list_cpy
    elif idx > length:
        return my_list_cpy
    else:
        my_list_cpy[idx] = element
        return my_list_cpy


if __name__ == "__main__":
    new_in_list(my_list, idx, element)
