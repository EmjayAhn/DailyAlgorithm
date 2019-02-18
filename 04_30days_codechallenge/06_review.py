# https://www.hackerrank.com/challenges/30-review-loop/problem

import sys
number = int(sys.stdin.readline().rstrip('\n'))

for _ in range(number):
    input_string = sys.stdin.readline().rstrip('\n')
    even_string = ''
    odd_string = ''
    for index, string in enumerate(input_string):
        if index % 2 == 0:
            even_string += string
        else:
            odd_string += string
    sys.stdout.write(even_string + ' ' + odd_string + '\n')