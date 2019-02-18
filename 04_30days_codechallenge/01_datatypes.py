# https://www.hackerrank.com/challenges/30-data-types/problem

import sys

i = 4
d = 4.0
s = 'HackerRank'

i_plus = int(sys.stdin.readline().rstrip('\n'))
d_plus = float(sys.stdin.readline().rstrip('\n'))
s_plus = sys.stdin.readline().rstrip('\n')
    
print(i + i_plus)
print(d + d_plus)
print(s + s_plus)
