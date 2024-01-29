#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for row in range(len(new_matrix)):
        for column in range(len(new_matrix[row])):
            new_matrix[row][column] = new_matrix[row][column] ** 2
    return new_matrix