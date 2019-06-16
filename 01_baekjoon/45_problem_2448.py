# https://www.acmicpc.net/problem/2448

import sys

input = sys.stdin.readline().rstrip('\n')
N = int(input)

stars = [' '*2 + '*' + ' '*2,' ' + '*' + ' ' + '*' + ' ', '*****']
for star in stars:
    print(star)