import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

each_day =  A - B

if (V-B) % (A-B) == 0:
    print((V-B) // (A-B))
else:
    print((V-B) // (A-B) + 1)
