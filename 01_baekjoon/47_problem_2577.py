# https://www.acmicpc.net/problem/2577

import sys
import collections

A = int(sys.stdin.readline().rstrip('\n'))
B = int(sys.stdin.readline().rstrip('\n'))
C = int(sys.stdin.readline().rstrip('\n'))

result = A * B * C

result = str(result)
counts = collections.Counter() 
counts.update(result)

for element in range(10):
    print(counts[str(element)])