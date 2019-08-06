# https://www.acmicpc.net/problem/2748

import sys

memory = {0: 0, 1: 1}

def fibo(num):
    if num not in memory:
        memory[num] = fibo(num - 1) + fibo(num - 2)
    return memory[num]

N = int(sys.stdin.readline().rstrip())
print(fibo(N))