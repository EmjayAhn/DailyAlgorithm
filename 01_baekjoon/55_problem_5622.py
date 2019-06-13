# https://www.acmicpc.net/problem/5622

import sys

input_word = sys.stdin.readline().rstrip('\n')

number_dict = {'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5, 'MNO': 6, \
    'PQRS': 7, 'TUV': 8, 'WXYZ': 9}

time = 0

for char in input_word:
    for key in number_dict.keys():
        if char in key:
            dial_number = number_dict[key]
            time += (dial_number + 1)
            break

print(time)