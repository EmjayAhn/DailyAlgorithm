# https://www.acmicpc.net/problem/10039

import sys

scores = []
for _ in range(5):
    input_score = int(sys.stdin.readline().rstrip('\n'))
    if input_score < 40:
        input_score = 40
    scores.append(input_score)
mean = sum(scores) // 5
print(mean)