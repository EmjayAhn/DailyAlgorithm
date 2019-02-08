# https://www.hackerrank.com/challenges/time-conversion/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import sys

def timeconversion(s):
    if s[-2:] == 'AM':
        if s[:2] == '12':
            return '00' + s[2:-2]
        return s[:-2]
    else:
        if s[:2] == '12':
            return '12' + s[2:-2]
        return str(int(s[:2]) + 12) + s[2:-2]


input_12 = sys.stdin.readline().rstrip('\n')
return_24 = timeconversion(input_12)

print(return_24)