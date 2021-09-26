import sys
N = int(sys.stdin.readline())

input_lists = []
for _ in range(N):
    input_cordinate = list(map(int, sys.stdin.readline().split()))
    input_lists.append(input_cordinate)

sorted_list = sorted(input_lists, key=lambda cordinate: ([cordinate[0], cordinate[1]]))

for cord in sorted_list:
    print(cord[0], cord[1])