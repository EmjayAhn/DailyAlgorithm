# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import sys
import math

def cumulative(input, mean, std):
    result = 0.5 * (1 + math.erf((input-mean)/(std * math.sqrt(2))))
    return result

input1 = list(map(float, sys.stdin.readline().rstrip('\n').split()))
mean = input1[0]
std = input1[1]
input2 = float(sys.stdin.readline().rstrip('\n'))
input3 = float(sys.stdin.readline().rstrip('\n'))

result1 = (1 - cumulative(input2, mean, std)) * 100
result2 = (1 - cumulative(input3, mean, std)) * 100
result3 = cumulative(input3, mean, std) * 100

sys.stdout.write(str(round(result1, 2)) + '\n' + str(round(result2,2)) + '\n' + str(round(result3, 2)))