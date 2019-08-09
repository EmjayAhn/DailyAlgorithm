# https://www.acmicpc.net/problem/7568

import sys

num_people = int(sys.stdin.readline().rstrip())
people_info = []
people_rate = []
for _ in range(num_people):
    x, y = list(map(int, sys.stdin.readline().rstrip().split()))
    people_info.append((x, y))

for weight, height in people_info:
    count = 0
    for other_weight, other_height in people_info:
        if (other_weight > weight) and (other_height > height):
            count += 1
    people_rate.append(count+1)

print(' '.join(map(str, people_rate)))



        