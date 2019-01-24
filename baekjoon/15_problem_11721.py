# https://www.acmicpc.net/problem/11721
# 백준 문제 11721

import sys

input_1 = sys.stdin.readline().rstrip('\n')
result = ''
for index in range(len(input_1)):
    if index == 0:
        result += input_1[index]
    else:
        if index%10 == 0:
            result += '\n'
        result += input_1[index]
print(result)
