import sys

inputs = []
for _ in range(9):
    input_number = int(sys.stdin.readline())
    inputs.append(input_number)
max_number = max(inputs)
print(max_number)
print(inputs.index(max_number)+1)
