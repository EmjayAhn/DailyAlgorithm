# https://www.acmicpc.net/problem/2108

import sys
import collections

N = int(input())

inputs = []
for _ in range(N):
    input_number = int(input())
    inputs.append(input_number)
inputs = sorted(inputs)
mean = round(sum(inputs) / len(inputs))
median = inputs[len(inputs) // 2]
c = sorted(collections.Counter(inputs).items(), key=lambda item: -item[1])
mode = c[0][0]
range_ = max(inputs) - min(inputs)

print(mean)
print(median)
print(mode)
print(range_)