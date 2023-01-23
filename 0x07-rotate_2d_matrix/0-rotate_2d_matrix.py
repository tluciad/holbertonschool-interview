#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """prototype - The matrix must be edited in-place."""

    end = len(matrix)
    for i in range(int(end/2)):
        start = (end - i - 1)
        for j in range(i, start):
            current = (end - 1 - j)
            temp = matrix[i][j]
            """changing top for left"""
            matrix[i][j] = matrix[current][i]
            """left to bottom"""
            matrix[current][i] = matrix[start][current]
            """bottom to right"""
            matrix[start][current] = matrix[j][start]
            """right to top"""
            matrix[j][start] = temp