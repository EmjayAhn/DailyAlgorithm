import sys
sys.setrecursionlimit(10000) 

def dfs(x, y):
    global adj_matrix
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if adj_matrix[nx][ny] == 1:
                adj_matrix[nx][ny] = -1
                dfs(nx, ny)
                
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    adj_matrix = [[0]*M for _ in range(N)]
    count = 0

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        adj_matrix[y][x] = 1
    
    for i in range(N):
        for j in range(M):
            if adj_matrix[i][j] > 0:
                dfs(i, j)
                count += 1
    print(count)
