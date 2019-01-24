# https://www.acmicpc.net/problem/11720
# 백준 문제 11720

import sys

input_1 = sys.stdin.readline().rstrip('\n')
input_2 = sys.stdin.readline().rstrip('\n')
result = 0
for index in range(int(input_1)):
    result += int(input_2[index])
print(result)
