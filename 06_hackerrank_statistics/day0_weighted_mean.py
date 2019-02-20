# https://www.hackerrank.com/challenges/s10-weighted-mean/problem?h_r=next-challenge&h_v=zen

import sys

def weighted_mean(xs, weights):
    weight_sum = 0
    for index, _ in enumerate(xs):
        weight_sum += (xs[index] * weights[index])
    return round(weight_sum / sum(weights), 1)

number_of_xs = int(sys.stdin.readline().rstrip('\n'))
xs = list(map(int, sys.stdin.readline().rstrip('\n').split()))
weights = list(map(int, sys.stdin.readline().rstrip('\n').split()))

sys.stdout.write(str(weighted_mean(xs, weights)) + '\n')



