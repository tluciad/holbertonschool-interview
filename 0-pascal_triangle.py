#!/usr/bin/python3
"""Create a function def pascal_triangle(n): that returns a list of lists of 
integers representing the Pascal’s triangle of n:"""


def pascal_triangle(n):
    """module function def pascal_triangle(n)"""
    triangle = []

    for i in range(n):
        triangle.append([])
        temp = 0

        for j in range(i + 1):
            if n <= 0:
                triangle = []
            elif j == 0 or j == i:
                triangle[i].append(1)
            else:
                temp = triangle[i - 1][j - 1] + triangle[i - 1][j]
                triangle[i].append(temp)

    return triangle
