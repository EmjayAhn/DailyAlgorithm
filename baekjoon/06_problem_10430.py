# https://www.acmicpc.net/problem/10430
# 백준 알고리즘 문제 10430

while True:
    try:
        a, b, c = map(int, input().split())
        print((a + b) % c)
        print(((a % c) + (b % c)) %c)
        print((a * b) % c)
        print((a % c * b % c) % c)
    except:
        break
