# https://www.acmicpc.net/problem/10430

import sys
inputs = sys.stdin.readline().rstrip('\n')
A, B, C = map(int, inputs.split())

result1 = (A + B) % C
result2 = ((A % C)+(B % C)) % C
result3 = (A * B) % C
result4 = ((A % C) * (B % C)) % C

print(result1)
print(result2)
print(result3)
print(result4)

