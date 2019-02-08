# https://www.hackerrank.com/challenges/plus-minus/problem

import sys
import math

def plusminus(arr):
    pos, neg, zer = 0, 0, 0
    for number in arr:
        if number > 0:
            pos += 1
        elif number < 0:
            neg += 1
        else:
            zer += 1
    print("{0:.6f}".format(pos/len(arr)))
    print("{0:.6f}".format(neg/len(arr)))
    print("{0:.6f}".format(zer/len(arr)))
size = int(sys.stdin.readline().rstrip('\n'))
arr = list(map(int, sys.stdin.readline().rstrip('\n').split()))
plusminus(arr)
