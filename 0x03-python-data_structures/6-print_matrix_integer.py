#!/usr/bin/python3

def print_matrix_integer(matrix = [[]]):

    for row in matrix:
        for i in range(len(row)):
            print(row[i], end="")
        print()


if __name__ == "__main__":
    print_matrix_integer(matrix = [[]])