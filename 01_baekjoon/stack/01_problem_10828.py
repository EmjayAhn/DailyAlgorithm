# https://www.acmicpc.net/problem/10828

import sys

def push(stack, param):
    stack.append(param)
    return stack

def pop(stack):
    if len(stack) == 0:
        print(-1)
    else:
        pop_result = stack.pop()
        print(pop_result)
    return stack


def size(stack):
    print(len(stack))


def empty(stack):
    if len(stack) == 0:
        print(1)
    else:
        print(0)


def top(stack):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])


N = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'push':
        param = command[1]
        command = command[0]
        stack = eval(command)(stack, param)
    else:
        command = command[0]
        eval(command)(stack)