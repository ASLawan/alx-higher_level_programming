#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def calculate():

    args = sys.argv
    num_args = len(args)
    if num_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(args[1])
        b = args[2]
        c = int(args[3])
        match b:
            case "+":
                print("{} {} {} = {}".format(a, b, c, add(a, c)))
            case "-":
                print("{} {} {} = {}".format(a, b, c, sub(a, c)))
            case "*":
                print("{} {} {} = {}".format(a, b, c, mul(a, c)))
            case "/":
                print("{} {} {} = {}".format(a, b, c. div(a, c)))
            case _:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)


if __name__ == "__main__":
    calculate()
