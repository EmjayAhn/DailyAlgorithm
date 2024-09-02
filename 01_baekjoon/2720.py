import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    input_number = int(input())
    Q = input_number // 25
    input_number = input_number % 25
    D = input_number // 10
    input_number = input_number % 10
    N = input_number // 5
    input_number = input_number % 5
    P = input_number // 1
    print(Q, D, N, P)