# https://www.hackerrank.com/challenges/staircase/problem?h_r=next-challenge&h_v=zen

import sys

def staircase(n):
    space = ' '
    sharp = '#'
    for number in range(1, n+1):
        print(space * (n - number) + sharp * number)
        
size = int(sys.stdin.readline().rstrip('\n'))
staircase(size)
