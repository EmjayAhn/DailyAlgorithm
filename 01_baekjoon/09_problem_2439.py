# https://www.acmicpc.net/problem/2439
# 백준 문제 2439

while True:
    try:
        input = int(input())
        for count in range(1, input+1):
            print(' ' * (input - count) + '*' * count)
    except:
        break
