# https://www.acmicpc.net/problem/1904

N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    init_1, init_2 = 1, 2
    for n in range(3, N+1):
        init_1, init_2 = init_2 % 15746, (init_1 + init_2) % 15746
    print(init_2 % 15746)