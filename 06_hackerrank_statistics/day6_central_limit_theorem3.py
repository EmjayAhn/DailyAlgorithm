# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import sys
import math

samples = int(sys.stdin.readline().rstrip('\n'))
mean = int(sys.stdin.readline().rstrip('\n'))
std = int(sys.stdin.readline().rstrip('\n'))
interval_prob = float(sys.stdin.readline().rstrip('\n'))
z_value = float(sys.stdin.readline().rstrip('\n'))

std = std / math.sqrt(samples)
A = (-z_value) * std + mean
B = z_value * std + mean

sys.stdout.write(str(round(A, 2)) + '\n' + str(round(B, 2)))