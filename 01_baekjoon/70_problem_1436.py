# https://www.acmicpc.net/problem/1436

N = int(input())

def title(N):
    count = 0
    value_check = 1
    while count < N:
        value_check += 1
        if '666' in str(value_check):
            count += 1
    return value_check


print(title(N))