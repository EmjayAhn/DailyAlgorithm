# https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

import sys

def is_prime(number):
    if number == 1:
        return 'Not prime'
    elif (number == 2) | (number == 3):
        return 'Prime'
    elif (number % 2 == 0) | (number % 3 == 0):
        return 'Not prime'
    else:
        i = 5
        while i * i <= number:
            if (number % i == 0) | (number % (i + 2) == 0):
                return 'Not prime'
            i += 6
    return 'Prime'

loop = int(sys.stdin.readline().rstrip('\n'))

for _ in range(loop):
    input = int(sys.stdin.readline().rstrip('\n'))
    result = is_prime(input)
    sys.stdout.write(str(result) + '\n')