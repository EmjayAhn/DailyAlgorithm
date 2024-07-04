# n! / (n-k)!k!

import sys
N, K = map(int, sys.stdin.readline().split())

def factorial(a):
    if a == 0:
        return 1
    if a == 1:
        return 1
    return a*factorial(a-1)

result = factorial(N) // (factorial(N-K)*factorial(K))

print(result)

