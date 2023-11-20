#!/usr/bin/python3

def magic_calculation(a, b):

    result = 1
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result = (result ** a) // (i * b) + b
        except Exception:
            print("Exception: Too far")
            return None
    return result + b
