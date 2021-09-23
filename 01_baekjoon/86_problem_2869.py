import sys

A, B, V = list(map(int, sys.stdin.readline().split()))
total_height = 0

days = (V-B) // (A-B)
remain =(V-B) % (A-B)

if remain > 0:
    days += 1

print(days)

