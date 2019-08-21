# https://www.acmicpc.net/problem/2075

N = int(input())

table = []

for _ in range(N):
    for number in input().split():
        table.append(int(number))
        if len(table) == (2 * N):
                table = sorted(table, reverse=True)[:N]
print(table[-1])