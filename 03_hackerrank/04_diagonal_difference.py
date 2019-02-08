# https://www.hackerrank.com/challenges/diagonal-difference/problem

import sys
import math

def diagonal_diff(arr):
    first_diag = 0
    second_diag = 0
    for index, row in enumerate(arr):
        first_diag += row[index]
        second_diag += row[len(arr)-index-1]
    return abs(first_diag - second_diag)

card = int(sys.stdin.readline().rstrip('\n'))
arr = list()
for _ in range(card):
    row = sys.stdin.readline().strip('\n')
    row = list(map(int, row.split()))
    arr.append(row)

print(diagonal_diff(arr)
)