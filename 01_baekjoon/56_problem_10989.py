# https://www.acmicpc.net/problem/10989

N = int(input())

inputs = []

for _ in range(N):
    input_number = int(input())
    inputs.append(input_number)

inputs = sorted(inputs)
for number in inputs:
    print(number)