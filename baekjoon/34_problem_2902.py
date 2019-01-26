# https://www.acmicpc.net/problem/2902
# 백준 문제 2902
import sys
input = sys.stdin.readline().rstrip('\n')
words = input.split('-')
result = ''
for word in words:
    result += word[0]
print(result)
