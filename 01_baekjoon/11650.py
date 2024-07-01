import sys
N = int(sys.stdin.readline())

input_cord = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    input_cord.append((x, y))
    
for each_cord in sorted(input_cord, key=lambda x: (x[0], x[1])):
    print(' '.join(map(str, [each_cord[0], each_cord[1]])))
    