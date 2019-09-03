# https://www.acmicpc.net/problem/2884

import sys

def early_clock(H, M):
    M = M - 45
    if M < 0:
        H = H - 1
        M = 60 + M
    if H < 0:
        H = 24 + H
    return H, M

H, M = map(int, sys.stdin.readline().rstrip().split())
H, M = early_clock(H, M)

print("{} {}".format(H, M))
