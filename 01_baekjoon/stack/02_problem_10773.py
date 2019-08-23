# https://www.acmicpc.net/problem/10773

import sys

def money(stack, param):
    if param == 0:
        stack.pop()
    else:
        stack.append(param)
    return stack

K = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(K):
    input_ = int(sys.stdin.readline().rstrip())
    stack = money(stack, input_)

print(sum(stack))

