# https://www.hackerrank.com/challenges/30-2d-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def hourglasssum(arr):
    total_sum = list()
    for i in range(0, 4):
            for j in range(0, 4):
                    total_sum.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
    return max(total_sum)

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

result = hourglasssum(arr)
print(result)