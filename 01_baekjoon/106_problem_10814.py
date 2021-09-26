import sys
N = int(sys.stdin.readline())

input_list = []

for _ in range(N):
    input_list.append(sys.stdin.readline().split())

sorted_list = sorted(input_list, key=lambda data: [int(data[0])])

for data in sorted_list:
    print(data[0], data[1])
    