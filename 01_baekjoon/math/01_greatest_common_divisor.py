# https://www.acmicpc.net/problem/2609

N, M = map(int, input().split())

divisors = []
multiples = []

divisor = 1
while divisor < min(N, M):
    if (N%divisor==0) & (M&divisor==0):
        divisors.append(divisor)
        divisor += 1
    else:
        divisor += 1

