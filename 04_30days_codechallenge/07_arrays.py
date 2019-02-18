# https://www.hackerrank.com/challenges/30-arrays/problem

import sys

n = int(sys.stdin.readline().rstrip('\n'))
arr = list(map(int, sys.stdin.readline().rstrip('\n').split()))
result = ''
for item in arr[::-1]:
    result += str(item)
    result += ' '
print(result)