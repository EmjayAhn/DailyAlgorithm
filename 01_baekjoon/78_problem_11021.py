# https://www.acmicpc.net/problem/11021

import sys

def sum_(a, b):
    return a + b

cases = int(sys.stdin.readline().rstrip())

for index in range(cases):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    result = sum_(A, B)
    print("Case #{}: {}".format(index+1, result))