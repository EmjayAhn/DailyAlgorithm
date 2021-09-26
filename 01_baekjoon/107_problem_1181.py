import sys

N = int(sys.stdin.readline())

input_list = []

for _ in range(N):
    input_list.append(sys.stdin.readline().rstrip())

sorted_list = sorted(list(set(input_list)), key=lambda data: (len(data), data))

for data in sorted_list:
    print(data)