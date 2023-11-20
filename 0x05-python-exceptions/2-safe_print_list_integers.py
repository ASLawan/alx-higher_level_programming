#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    count = 0
    for list_item in range(x):
        try:
            print("{:d}".format(my_list[list_item]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
        except IndexError:
            raise
    print()
    return count


if __name__ == "__main__":
    safe_print_list_integers(my_list=[], x=0)
