# https://www.acmicpc.net/problem/2953
# 나는 요리사다

import sys

inputs = []
for _ in range(5):
    input_ = list(map(int, sys.stdin.readline().split()))
    inputs.append(input_)

results = list(map(sum, inputs))

max_value = max(results)
max_index = results.index(max_value)

print(max_index+1, max_value)