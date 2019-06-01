# https://www.acmicpc.net/problem/2441

import sys

input = sys.stdin.readline().rstrip('\n')

N = int(input)
for number in range(N):
    space = number
    stars = N - number
    print(' ' * space + '*' * stars)