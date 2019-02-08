# https://www.acmicpc.net/problem/11365
# 백준 문제 11365
import sys
while True:
    strings = sys.stdin.readline().rstrip('\n')
    if strings == 'END':
        break
    result = ''
    for string in strings:
        result = string + result
    print(result)
