# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem?h_r=next-challenge&h_v=zen

import sys
import math

def cumulative(input, mean, std):
    result = 0.5 * (1 + math.erf((input-mean)/(std * math.sqrt(2))))
    return result
input1 = list(map(float, sys.stdin.readline().rstrip('\n').split()))
mean = input1[0]
std = input1[1]
input2 = float(sys.stdin.readline().rstrip('\n'))
input3 = list(map(float, sys.stdin.readline().rstrip('\n').split()))
integrate_from = input3[0]
integrate_to = input3[1]

result1 = cumulative(input2, mean, std)
result2 = cumulative(integrate_to, mean, std) - cumulative(integrate_from, mean, std)

sys.stdout.write(str(round(result1, 3)) + '\n' + str(round(result2, 3)))