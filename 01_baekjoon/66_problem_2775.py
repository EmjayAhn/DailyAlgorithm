# https://www.acmicpc.net/problem/2775

import sys

num_cases = int(sys.stdin.readline().rstrip())

memory = {(0, i): i for i in range(1, 15)}

def find_num_people(k, n):
    if (k, n) in memory:
        return memory[(k, n)]

    else:
        memory[(k, n)] = 0
        for room in range(1, n+1):
            memory[(k, n)] += find_num_people(k-1, room)

        return memory[(k, n)]

for _ in range(num_cases):
    k = int(input())
    n = int(input())
    print(find_num_people(k, n))
