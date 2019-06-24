# https://www.acmicpc.net/problem/2581

M = int(input())
N = int(input())
numbers = [number for number in range(M, N+1)]
prime_results = []
prime_numbers = []

def is_prime(number):
    if number == 1:
        return 0
    for divisor in range(2, number):
        if (number % divisor) == 0:
            return 0
    return 1

for number in numbers:
    result = is_prime(number)
    prime_results.append(result)

for number, result in zip(numbers, prime_results):
    prime_numbers.append(number * result)

prime_numbers = list(set(prime_numbers))
prime_numbers.remove(0)
if len(prime_numbers) == 0:
    print(-1)
else:
    print(sum(prime_numbers))
    print(min(prime_numbers))