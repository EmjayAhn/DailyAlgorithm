# https://www.acmicpc.net/problem/1330

import sys

m, n = map(int, sys.stdin.readline().rstrip().split())

if m < n:
    print("<")
elif m > n:
    print(">")
else:
    print("==")
