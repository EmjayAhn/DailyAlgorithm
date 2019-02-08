# https://www.acmicpc.net/problem/9498
# 백준 문제 9498

import sys

input = int(sys.stdin.readline().rstrip('\n'))
if (input >= 90) & (input <= 100):
    print("A")
elif (input >= 80) & (input <= 89):
    print("B")
elif (input >= 70) & (input <= 79):
    print("C")
elif (input >= 60) & (input <= 69):
    print("D")
else:
    print("F")
