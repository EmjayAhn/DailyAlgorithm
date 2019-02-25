# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem

import sys
import math

def cumulative(input, mean, std):
    result = 0.5 * (1 + math.erf((input-mean)/(std * math.sqrt(2))))
    return result

maximum_cap = int(sys.stdin.readline().rstrip('\n'))
box_num = int(sys.stdin.readline().rstrip('\n'))
box_mean = int(sys.stdin.readline().rstrip('\n'))
box_std = int(sys.stdin.readline().rstrip('\n'))

sum_mean = box_num * box_mean
sum_std = (box_num ** 0.5) * box_std

probability = cumulative(9800, sum_mean, sum_std)

sys.stdout.write(str(round(probability, 4)))