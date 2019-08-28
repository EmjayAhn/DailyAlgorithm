# https://www.acmicpc.net/problem/10845

import sys

def push(queue, param):
    queue.append(param)
    return queue

def pop(queue):
    if len(queue) == 0:
        print(-1)
    else:
        pop_result = queue.pop(0)
        print(pop_result)
    return queue


def size(queue):
    print(len(queue))


def empty(queue):
    if len(queue) == 0:
        print(1)
    else:
        print(0)


def front(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])

def back(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])
        

N = int(sys.stdin.readline().rstrip())
queue = []
for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'push':
        param = command[1]
        command = command[0]
        queue = eval(command)(queue, param)
    else:
        command = command[0]
        eval(command)(queue)

