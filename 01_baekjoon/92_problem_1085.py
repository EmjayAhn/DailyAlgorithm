import sys

x, y, w, h = map(int, sys.stdin.readline().split())

horizon = w - x
vertical = h - y

answer = min(x, y, horizon, vertical)
print(answer)
