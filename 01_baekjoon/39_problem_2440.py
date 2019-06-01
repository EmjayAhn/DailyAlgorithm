# https://www.acmicpc.net/problem/2440

import sys
input = sys.stdin.readline().rstrip('\n')
N = int(input)

for number in range(N):
    result = N - number
    print('*' * result)