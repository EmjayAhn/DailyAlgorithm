# https://www.acmicpc.net/problem/10951

import sys

def sum_(a, b):
    return a + b

while True:
    try:
        A, B = map(int, sys.stdin.readline().rstrip().split())
        print(sum_(A, B))
    except:
        break