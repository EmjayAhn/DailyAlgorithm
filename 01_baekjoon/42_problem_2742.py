# https://www.acmicpc.net/problem/2742

import sys

input = sys.stdin.readline().rstrip('\n')

N = int(input)
for number in list(range(N+1))[:0:-1]:
    print(number)