#!/usr/bin/python3
"""solvin N queens puzzle"""
import sys

if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
try:
    N = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)
if N < 4:
    print('N must be at least 4')
    exit(1)

row = 0
count_row = 2
for i in range(N-2):
    res = []
    count_row += 1
    n = row
    for col in range(N):
        res.append([col, row])
        if (row + count_row > N-1):
            row += count_row - 1 - N
        else:
            row += count_row
    print(res)
    count_row += 1
    row = n
exit(0)
   