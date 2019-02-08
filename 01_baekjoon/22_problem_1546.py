# https://www.acmicpc.net/problem/1546
# 백준 문제

import sys
input1 = sys.stdin.readline().rstrip('\n')
input2 = sys.stdin.readline().rstrip('\n')
input2 = list(map(int, input2.split()))
max = max(input2)
average = sum(input2) / len(input2)
print(round(average / max * 100, 2))
