import sys

def stars(N, pattern):    
    # escape condition
    if N == 3:
        pattern[0][:3] = pattern[2][:3] = ['*', '*', '*']
        pattern[1] = ['*', ' ', '*']        
        return pattern
    
    Div = N // 3
    stars(Div, pattern)

    for i in range(0, N, Div):
        for j in range(0, N, Div):
            if (i != Div) or (j !=Div):
                for k in range(Div):
                    pattern[i+k][j:j+Div] = pattern[k][:Div]
    
    return pattern


N = int(sys.stdin.readline())
pattern = [[' ' for _ in range(N)] for _ in range(N)]

pattern = stars(N, pattern)

for i in range(N):
    for j in range(N):
        print(pattern[i][j], end='')
# sys.setrecursionlimit(10**6)