#!/usr/bin/python3
def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    temp = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if temp != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        temp = len(row)

    new_list = [row[:] for row in matrix]

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if type(matrix[row][column]) is not int and type(matrix[row][column]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            result = (matrix[row][column]/div)
            new_list[row][column] = ('{:.2f}'.format(result))
    
    return new_list
