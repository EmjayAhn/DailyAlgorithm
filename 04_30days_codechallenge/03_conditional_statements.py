# https://www.hackerrank.com/challenges/30-conditional-statements/problem

import sys

def solve(n):
    if (n % 2) == 1:
        return 'Weird'
    else:
        if (n >= 2) & (n <= 5):
            return 'Not Weird'
        elif (n >= 6) & (n <= 20):
            return 'Weird'
        elif n > 20:
            return 'Not Weird'
    
n = int(sys.stdin.readline().rstrip('\n'))
result = solve(n)
print(result)

