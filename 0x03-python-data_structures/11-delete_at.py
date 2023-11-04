#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

    length = len(my_list)
    if idx < 0 or idx > length - 1:
        return my_list
    for i in range(length):
        if i == idx:
            del my_list[i]

    return my_list


if __name__ == "__main__":
    delete_at(my_list=[], idx=0)
