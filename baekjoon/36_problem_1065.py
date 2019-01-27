# https://www.acmicpc.net/problem/1065
# 백준 문제 1065

import sys
input = sys.stdin.readline().rstrip('\n')

sign = 0
count = 0
if len(input) <= 2:
    count = int(input)
else:
    for number in range(100, int(input) + 1):
        equal_sub = 0
        number = str(number)
        for index in range(len(number)-2):
            mem1 = int(number[index]) - int(number[index+1])
            mem2 = int(number[index+1]) - int(number[index+2])
            if mem1 == mem2:
                equal_sub += 1
        if equal_sub == len(number) - 2:
            count += 1
    count += 99
print(count)
