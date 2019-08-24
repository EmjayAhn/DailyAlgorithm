# https://www.acmicpc.net/problem/17298

import sys

N = int(sys.stdin.readline().rstrip())
stack = list(map(int, sys.stdin.readline().rstrip().split()))

result = ""
for index, number in enumerate(stack):
    candidates = []
    for candi in stack[index+1:]:
        if (number < candi):
            candidates.append(candi)
    if candidates:
        result += str(candidates[0]) + ' '
    else:
        result += '-1' + ' '

print(result)

    

