# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem?h_r=next-challenge&h_v=zen

import sys
import math

def nCr(n, r):
    f = math.factorial
    result = f(n) / (f(n-r) * f(r))
    return result

def binomial(input):
    defect_ratio = input[0] / 100
    batch = input[1]
    answer1 = 0
    answer2 = 0
    for rejects in range(0, 3):
        answer1 += nCr(batch, rejects) * (defect_ratio ** rejects) * ((1-defect_ratio) ** (batch - rejects))
    for rejects in range(0, 2):
        answer2 += nCr(batch, rejects) * (defect_ratio ** rejects) * ((1-defect_ratio) ** (batch - rejects))
    answer2 = 1 - answer2
    return answer1, answer2

input = list(map(float, sys.stdin.readline().rstrip('\n').split()))
result = binomial(input)

sys.stdout.write(str(round(result[0], 3)) + '\n' + str(round(result[1], 3)))
