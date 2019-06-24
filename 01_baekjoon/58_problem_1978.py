# https://www.acmicpc.net/problem/1978

N = int(input())
numbers = list(map(int, input().split()))

results = []

def is_prime(number):
    if number == 1:
        return 0
    for divisor in range(2, number):
        if (number % divisor) == 0:
            return 0
    return 1

for number in numbers:
    result = is_prime(number)
    results.append(result)

print(sum(results))
