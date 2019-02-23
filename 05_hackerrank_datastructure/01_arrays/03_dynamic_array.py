# https://www.hackerrank.com/challenges/dynamic-array/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    seq_list = [[] for _ in range(n)]
    lastAnswer = 0
    result = []
    for query in queries:
        seq_index = (query[1]^lastAnswer) % n
        if query[0] == 1:
            seq_list[seq_index].append(query[2])
        elif query[0] == 2:
            lastAnswer = seq_list[seq_index][query[2] % len(seq_list[seq_index])]
            result.append(lastAnswer)
    return result

if __name__ == '__main__':
    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print('\n'.join(map(str, result)))