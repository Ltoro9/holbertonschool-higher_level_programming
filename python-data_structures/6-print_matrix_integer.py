#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in range(len(row)):
            if column == len(row) - 1:
                print("{:d}".format(row[column]))
            else:
                print("{:d}".format(row[column]), end=' ')
