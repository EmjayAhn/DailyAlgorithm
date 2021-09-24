import sys

def prime_number(n):
    div = 2
    if n == 1:
        return False
    while(True):
        if div > n**0.5:
            break
        if n % div == 0:
            return False
        div += 1
    return True

M, N = map(int, sys.stdin.readline().split())

prime_numbers = []
for number in range(M, N+1):
    if prime_number(number):
        prime_numbers.append(number)

for number in prime_numbers:
    print(number)

