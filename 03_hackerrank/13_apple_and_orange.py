# https://www.hackerrank.com/challenges/apple-and-orange/problem

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # s, t : location of Sam's house start & end
    # a : location of apple tree
    # b : location of orange tree
    # apples: array (vector)
    # oranges: array (vector)
    sam_apples = 0
    sam_oranges = 0

    for apple_distance in apples:
        apple_location = apple_distance + a
        if (apple_location >= s) & (apple_location <= t):
            sam_apples += 1
    for orange_distance in oranges:
        orange_location = orange_distance + b
        if (orange_location >= s) & (orange_location <= t):
            sam_oranges += 1
    
    print(sam_apples)
    print(sam_oranges)


# the below variable names are given by hackerrank which is not my naming style
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
