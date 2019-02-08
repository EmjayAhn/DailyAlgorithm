# https://www.hackerrank.com/challenges/mini-max-sum/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import sys

def minimaxsum(arr):
    total = sum(arr)
    arr = sorted(arr)
    maxi = total - arr[0]
    mini = total - arr[-1]
    print(mini, maxi)
    
arr = list(map(int, sys.stdin.readline().rstrip('\n').split()))
minimaxsum(arr)
