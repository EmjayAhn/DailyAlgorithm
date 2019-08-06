# https://www.acmicpc.net/problem/2747

import sys

mem = {0: 0, 1: 1}
def fibo(num):
    if num not in mem:
        mem[num] = fibo(num-1) + fibo(num-2)
    return mem[num]


N = int(input())
print(fibo(N))


