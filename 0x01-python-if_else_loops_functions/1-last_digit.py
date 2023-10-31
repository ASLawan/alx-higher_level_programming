#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    l_dgt = number % 10
else:
    l_dgt = number % -10
print("Last digit of {} ".format(number), end="")
if l_dgt > 5:
    print("is {} and is greater than 5".format(l_dgt))
elif l_dgt == 0:
    print("is {} and is 0".format(l_dgt))
elif:
    print("is {} and is less than 6 and not 0".format(l_dgt))
