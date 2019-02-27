# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

import sys

def pearson_std(X, Y):
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
    return pearson_correlation, std_X, std_Y

input_X = list()
input_Y = list()
for _ in range(5):
    input = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    input_X.append(input[0])
    input_Y.append(input[1])

pearson_corr, std_X, std_Y = pearson_std(input_X, input_Y)

slope = pearson_corr * std_Y / std_X
coef = (sum(input_Y) / len(input_Y)) - slope * (sum(input_X) / len(input_X))

result = 80 * slope + coef
sys.stdout.write(str(round(result, 3)))
