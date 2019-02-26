# https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem?h_r=next-challenge&h_v=zen

import sys

def spearman(X, Y):
    difference = list()
    sort_X = sorted(X)
    sort_Y = sorted(Y)
    for index, _ in enumerate(X):
        r_x = sort_X.index(X[index]) + 1
        r_y = sort_Y.index(Y[index]) + 1
        difference.append(r_x - r_y)
    difference_square = list(map(lambda i: i*i, difference))
    spearman = 1 - (6 * sum(difference_square) / (len(X) * (len(X) ** 2 - 1)))
    return spearman

_ = sys.stdin.readline().rstrip('\n')
X = list(map(float, sys.stdin.readline().rstrip('\n').split()))
Y = list(map(float, sys.stdin.readline().rstrip('\n').split()))

result = spearman(X, Y)
sys.stdout.write(str(round(result, 3)))
