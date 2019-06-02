# https://codeup.kr/problem.php?id=1079

import sys
input_strings = sys.stdin.readline().rstrip('\n')
input_strings = input_strings.split()
for string in input_strings:
    print(string)
    if string == 'q':
        break