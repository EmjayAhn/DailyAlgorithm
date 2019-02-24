# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

import sys
import math

def poisson_squaremean(mean):
    return mean + (mean ** 2)

input_list = list(map(float, sys.stdin.readline().rstrip('\n').split()))

X_mean = input_list[0]
Y_mean =  input_list[1]

sys.stdout.write(str(round(40 * poisson_squaremean(X_mean) + 160, 3)) + '\n' + str(round(40 * poisson_squaremean(Y_mean) + 128, 3)))
    