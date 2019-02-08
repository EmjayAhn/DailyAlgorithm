# https://www.hackerrank.com/challenges/a-very-big-sum/problem?h_r=next-challenge&h_v=zen

import sys

def aVeryBigSum(ar):
    return sum(ar)
    
how_many = int(sys.stdin.readline().rstrip('\n'))
numbers = sys.stdin.readline().rstrip('\n')
numbers = list(map(int, numbers.split()))
result = aVeryBigSum(numbers)
print(result)