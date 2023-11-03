#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    num = len(my_list)
    if idx < 0:
        return my_list
    elif idx > num:
        return my_list
    else:
        my_list[idx] = element
        return my_list


if __name__ == "__main__":
    replace_in_list(my_list, idx, element)
