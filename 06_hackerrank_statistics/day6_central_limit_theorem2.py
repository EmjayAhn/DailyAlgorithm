# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem?h_r=next-challenge&h_v=zen

import sys
import math

def cumulative(input, mean, std):
    result = 0.5 * (1 + math.erf((input-mean)/(std * math.sqrt(2))))
    return result

ticket_left = int(sys.stdin.readline().rstrip('\n'))
students = int(sys.stdin.readline().rstrip('\n'))
purchase_mean = float(sys.stdin.readline().rstrip('\n'))
purchase_std = float(sys.stdin.readline().rstrip('\n'))

all_purchase_mean = students * purchase_mean
all_purchase_std = math.sqrt(students) * purchase_std

result_prob = cumulative(250, all_purchase_mean, all_purchase_std)

sys.stdout.write(str(round(result_prob, 4)))
