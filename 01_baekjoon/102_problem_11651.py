import sys

N = int(sys.stdin.readline())

all_cordinates = []
for _ in range(N):
    input_cord = list(map(int, sys.stdin.readline().split()))
    all_cordinates.append(input_cord)

sorted_cordinates = sorted(all_cordinates, key=lambda value: [value[1], value[0]])

for cord in sorted_cordinates:
    print(cord[0], cord[1])
