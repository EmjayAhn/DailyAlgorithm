import sys
N = int(sys.stdin.readline())

total_list = [0] * 10001

for i in range(N):
    input_number = int(sys.stdin.readline())
    total_list[input_number] += 1

for i in range(10001):
    if total_list[i] != 0:
        for j in range(total_list[i]):
            print(i)
