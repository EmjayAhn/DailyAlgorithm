import sys

N = int(sys.stdin.readline())
inputs = list(map(int, sys.stdin.readline().split()))

print(min(inputs), max(inputs))

