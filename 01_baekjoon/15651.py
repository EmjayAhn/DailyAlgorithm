import sys

N, M = map(int, sys.stdin.readline().split())

string_list = []

def dfs():
    if len(string_list) == M:
        print(' '.join(map(str, string_list)))
        return

    for i in range(1, N+1):
        string_list.append(i)
        dfs()
        string_list.pop()

dfs()
        

