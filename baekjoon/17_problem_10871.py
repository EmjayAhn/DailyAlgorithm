# https://www.acmicpc.net/problem/10871
# 백준 문제 10871
import sys

input_1 = sys.stdin.readline().rstrip('\n')
input_2 = sys.stdin.readline().rstrip('\n')

N, X = map(int, input_1.split())
A = list(map(int, input_2.split()))

result = ''
for item in A:
    if item < X:
        result += (str(item) + ' ')
print(result)
