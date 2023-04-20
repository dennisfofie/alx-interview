#!/usr/bin/python3
"""
   Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n Returns an empty list if n <= 0 You can assume n will be always an integer 
"""


def find_factorial(n):
    """
    @n: number of which it factorial will be find and it is of type int

    Description - returns the factorial of n passed to it eg. when n is 5 , the output should be 5x4x3x2x1 = 120
    """
    total = 1
    if n == 1:
        return total

    for i in range(1, n + 1):
        total *= i
    return total


def pascal_triangle(n):
    """
    @n: number of rows of the pascal triangle
    Description - returns the pascal triangle with element of each row in list
    Approch - using combination formula
    time-complexity - n^2
    space: n
    """
    n = int(n)
    if n <= 0:
        return []

    result = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            res = find_factorial(i) // (find_factorial(i - j) * find_factorial(j))
            result[i].append(res)
    return result
