#!/usr/bin/python3

def uniq_add(my_list=[]):

    if not my_list:
        return 0
    else:
        new_list = []
        sum = 0
        for i in range(len(my_list)):
            if my_list[i] not in new_list:
                new_list.append(my_list[i])

        for i in range(len(new_list)):
            sum += new_list[i]

    return sum


if __name__ == "__main__":
    uniq_add(my_list=[])
