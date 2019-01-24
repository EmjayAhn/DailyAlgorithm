# https://www.acmicpc.net/problem/10952
# 백준 문제 10952

import sys

while True:
    inputs = sys.stdin.readline().rstrip('\n')
    A, B = map(int, inputs.split())
    result = A + B
    if (A == 0) & (B == 0):
        break
    print(result)
