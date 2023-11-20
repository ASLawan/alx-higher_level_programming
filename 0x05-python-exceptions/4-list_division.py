#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    for i in range(list_length):

        try:
            list_item = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            list_item = 0
        except (TypeError, ValueError):
            print("wrong type")
            list_item = 0
        except IndexError:
            print("out of range")
            list_item = 0
        finally:
            new_list.append(list_item)

    return new_list
