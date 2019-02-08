# https://www.acmicpc.net/problem/2941
# 백준 문제 2941
import sys

input = sys.stdin.readline().rstrip('\n')
cr_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'z=', 's=', 'nj']
for cr_alphabet in cr_alphabets:
    input = input.replace(cr_alphabet, '1')
print(len(input))
