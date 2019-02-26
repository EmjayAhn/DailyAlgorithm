# https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem

import sys

def pearson(X, Y):
    pearson_correlation = 0
    mean_X = sum(X) / len(X)
    mean_Y = sum(Y) / len(Y)
    mean_reduce_X_squared = list(map(lambda i: (i - mean_X)**2, X))
    mean_reduce_Y_squared = list(map(lambda i: (i - mean_Y)**2, Y))
    std_X = (sum(mean_reduce_X_squared) / len(X)) ** 0.5
    std_Y = (sum(mean_reduce_Y_squared) / len(Y)) ** 0.5
    mean_reduce_X = list(map(lambda i: i - mean_X, X))
    mean_reduce_Y  = list(map(lambda i: i - mean_Y, Y))
    for index, _ in enumerate(mean_reduce_X):
        pearson_correlation += mean_reduce_X[index] * mean_reduce_Y[index]
    pearson_correlation = pearson_correlation / (len(X) * std_X * std_Y)
    return pearson_correlation

_ = sys.stdin.readline().rstrip('\n')
X = list(map(float, sys.stdin.readline().rstrip('\n').split()))
Y = list(map(float, sys.stdin.readline().rstrip('\n').split()))

result = pearson(X, Y)
sys.stdout.write(str(round(result, 3)))

