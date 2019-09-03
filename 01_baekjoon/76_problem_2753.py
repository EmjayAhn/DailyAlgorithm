# https://www.acmicpc.net/problem/2753

import sys

def yun_year(year):
    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        return 1
    return 0

year = int(sys.stdin.readline().rstrip())
print(yun_year(year))