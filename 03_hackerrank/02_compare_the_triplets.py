# https://www.hackerrank.com/challenges/compare-the-triplets/problem

import sys

def solution(a, b):
    count_a = 0
    count_b = 0
    for index, _ in enumerate(a):
        if a[index] > b[index]:
            count_a += 1
        elif a[index] < b[index]:
            count_b += 1
    return count_a, count_b

a = sys.stdin.readline().rstrip('\n')
b = sys.stdin.readline().rstrip('\n')
a = list(map(int, a.split()))
b = list(map(int, b.split()))
result_a, result_b = solution(a, b) 
print(result_a, result_b)
