# https://www.hackerrank.com/challenges/simple-array-sum/problem

import sys

def solution(li):
    return sum(li)

input1 = sys.stdin.readline().rstrip('\n')
input2 = sys.stdin.readline().rstrip('\n')
input2 = list(map(int, input2.split()))
result = solution(input2)
print(result)