#!/usr/bin/python3

def weight_average(my_list=[]):

    sum = 0
    weight_sum = 0
    if my_list:
        for item in my_list:
            sum += (item[0] * item[1])
            weight_sum += item[1]

        average = sum / weight_sum
    else:
        return 0
    
    return average


if __name__ == "__main__":
    weight_average(my_list=[])
