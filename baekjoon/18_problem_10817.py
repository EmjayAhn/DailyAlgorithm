# https://www.acmicpc.net/problem/10817
# 백준 문제 10817
import sys

input_1 = sys.stdin.readline().rstrip('\n')
input_1 = sorted(list(map(int, input_1.split())), reverse=True)
print(input_1[1])
