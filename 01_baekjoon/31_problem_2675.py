# https://www.acmicpc.net/problem/2675
# 백준 문제 2675
import sys

input1 = int(sys.stdin.readline().rstrip('\n'))
for _ in range(input1):
    input2 = sys.stdin.readline().rstrip('\n')
    number, strings = input2.split()
    number = int(number)
    result = ''
    for string in strings:
        result += string * number
    print(result)
