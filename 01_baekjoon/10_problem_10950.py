# https://www.acmicpc.net/problem/10950
# 백준 문제 10950

while True:
    try:
        number_of_iteration = int(input())
        for _ in range(1, number_of_iteration + 1):
            a, b = map(int, input().split())
            print(a + b)
    except:
        break
