# https://www.acmicpc.net/problem/2438
# 백준 문제 2438

while True:
    try:
        input = int(input())
        for count in range(1, input + 1):
            print("*" * count)
    except:
        break
