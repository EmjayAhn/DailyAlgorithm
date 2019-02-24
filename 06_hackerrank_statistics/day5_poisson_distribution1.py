# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/tutorial

import sys
import math

def poisson(k, mean):
    return (mean**k) * (math.e ** (-mean)) / math.factorial(k)

mean = float(sys.stdin.readline().rstrip('\n'))
k = int(sys.stdin.readline().rstrip('\n'))
result = poisson(k, mean)

sys.stdout.write(str(round(result, 3)))