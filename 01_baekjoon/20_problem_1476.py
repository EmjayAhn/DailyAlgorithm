# https://www.acmicpc.net/problem/1476
# 백준 문제 1476
import sys

input = sys.stdin.readline().rstrip('\n')
e, s, m = map(int, input.split())
e %= 15
s %= 28
m %= 19
year_count = 1
while True:
    if (year_count % 15 == e) & (year_count % 28 == s) & (year_count % 19 == m):
        print(year_count)
        break
    year_count += 1
