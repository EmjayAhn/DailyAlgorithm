# https://www.acmicpc.net/problem/1002

import sys
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def num_position(distance, r1, r2):
    if distance == 0:
        if r1 == r2:
            return -1
        else:
            return 0
    else:
        if distance > r1 + r2:
            return 0

        elif (distance == r1 + r2) or (distance == abs(r1 - r2)):
            return 1

        elif distance < r1 + r2:
            if distance + min(r1, r2) < max(r1, r2):
                return 0
            else:
                return 2

num_iters = int(sys.stdin.readline().rstrip())
for _ in range(num_iters):
    inputs = list(map(int, sys.stdin.readline().rstrip().split()))
    x1, y1, r1, x2, y2, r2 = inputs

    dist_12 = distance(x1, y1, x2, y2)
    print(num_position(dist_12, r1, r2))