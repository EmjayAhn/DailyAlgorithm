# https://www.acmicpc.net/problem/8393

import sys

input = sys.stdin.readline().rstrip('\n')

n = int(input)
result = int(n*(n+1)/2)
print(result)