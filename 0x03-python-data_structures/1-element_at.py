#!/usr/bin/python3

def element_at(my_list, idx):

    num = len(my_list) - 1
    if idx < 0:
        return None
    elif idx > num:
        return None
    else:
        return my_list[idx]


if __name__ == "__main__":
    element_at(my_list, idx)
