import sys
input = sys.stdin.readline

H, M = map(int, input().split())
add = int(input())

M += add
H = H + M // 60
H = H % 24
M = M % 60


print(H, M)
