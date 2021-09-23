import sys

inputs = []
for _ in range(10):
    input_number = int(sys.stdin.readline())
    inputs.append(input_number%42)

print(len(list(set(inputs))))


