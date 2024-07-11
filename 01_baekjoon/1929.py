import sys
from math import sqrt
def is_prime(n):
    divisors = set()
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    result = True if len(divisors) == 2 else False
    return result
         
M, N = map(int, sys.stdin.readline().split())

for each_number in range(M, N + 1):
    if is_prime(each_number):
        print(each_number) 