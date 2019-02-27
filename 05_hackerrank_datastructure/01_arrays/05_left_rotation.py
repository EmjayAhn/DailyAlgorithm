# https://www.hackerrank.com/challenges/array-left-rotation/problem

import sys

def left_rotation(array, d):
    for _ in range(d):
        array.append(array.pop(0))
    return array

nd = sys.stdin.readline().rstrip('\n').split()
n = nd[0]
d = int(nd[1])

array = list(map(int, sys.stdin.readline().rstrip('\n').split()))

result = left_rotation(array, d)
result = list(map(str, result))
result = ' '.join(result)
print(result)