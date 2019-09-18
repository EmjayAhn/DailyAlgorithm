# https://www.acmicpc.net/problem/11047

import sys

def min_usage(units, target):
    units = sorted(units, reverse=True)
    result = 0
    for unit in units:
        if target > unit:
            quota = target // unit
            result += quota
            target -= (quota * unit)
            
    return result


N, target = map(int, sys.stdin.readline().rstrip().split())
units = []
for _ in range(N):
    unit = int(sys.stdin.readline().rstrip())
    units.append(unit)

result = min_usage(units, target)
print(result)
