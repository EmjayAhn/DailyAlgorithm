import sys

N = int(sys.stdin.readline().rstrip())

input_list = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    input_list.append((x, y))
    
input_list = sorted(input_list, key=lambda coordinate: (coordinate[1], coordinate[0]))

for each in input_list:
    print(' '.join(map(str, each)))
    