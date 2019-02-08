# https://www.acmicpc.net/problem/2839
# 백준 문제 2839
import sys

input = sys.stdin.readline().rstrip('\n')
input = int(input)
quotient_three = 0
quotient_five = 0
while True:
    if input % 5 == 0:
        quotient_five = input // 5
        print(quotient_five + quotient_three)
        break
    input = input - 3
    quotient_three += 1
    if input < 0:
        print(-1)
        break
