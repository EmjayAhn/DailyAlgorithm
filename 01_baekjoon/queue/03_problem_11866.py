# https://www.acmicpc.net/problem/11866

import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

josephus = [i for i in range(1, N+1)]
result = ''

while True:
    if len(josephus) == 0:
        break
    temp = josephus[:K-1]
    josephus = josephus[K-1:] + temp

    result += str(josephus.pop(0))

result = ', '.join(result)
print('<' + result + '>')