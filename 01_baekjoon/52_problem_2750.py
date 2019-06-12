# https://www.acmicpc.net/problem/2750

import sys

N = int(sys.stdin.readline().rstrip('\n'))
inputs = []
for _ in range(N):
    input_number = int(sys.stdin.readline().rstrip('\n'))
    inputs.append(input_number)

inputs = sorted(inputs)
for number in inputs:
    print(number)