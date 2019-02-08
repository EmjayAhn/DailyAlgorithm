# https://www.acmicpc.net/problem/2739
# 백준 문제 2739

while True:
    try:
        input = int(input())
        for mul in range(1, 10):
            print("{} * {} = {}".format(input, mul, input*mul))
    except:
        break
