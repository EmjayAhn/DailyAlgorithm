# https://www.hackerrank.com/challenges/s10-multiple-linear-regression/problem

import sys
from sklearn import linear_model

X = list()
Y = list()
mn = list(map(int, sys.stdin.readline().rstrip('\n').split()))
for _ in range(mn[1]):
    input = list(map(float, sys.stdin.readline().rstrip('\n').split()))
    X.append(input[0:-1])
    Y.append(input[-1])

lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_

test = int(sys.stdin.readline().rstrip('\n'))
for _ in range(test):
    result = 0
    test_case = list(map(float, sys.stdin.readline().rstrip('\n').split()))
    for index, _ in enumerate(b):
        result += b[index] * test_case[index]
    result += a
    print(result)
