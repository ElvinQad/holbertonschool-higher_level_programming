#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in matrix:
        if len(row) == 0:
            print()
        else:
            for i, element in enumerate(row):
                if i == len(row) - 1:
                    print("{:d}".format(element))
                else:
                    print("{:d}".format(element), end=" ") 
                
                