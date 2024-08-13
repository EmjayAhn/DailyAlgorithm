import sys
input = sys.stdin.readline

def get_best():
    global N, matrix
    best = 0
    
    for i in range(N):
        count = 1
        before = '-'
        for j in range(N):
            cur = matrix[i][j]
            if before == cur:
                count += 1
            else:
                count = 1
            before = cur
            best = max(best, count)
            
            
    for j in range(N):
        count = 1
        before = '-'
        for i in range(N):
            cur = matrix[i][j]
            if before == cur:
                count += 1
            else:
                count = 1
            before = cur
            best = max(best, count)
            
    return best            
            

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(input().rstrip()))

ans = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for y in range(N):
    for x in range(N):
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if matrix[y][x] != matrix[nx][nx]:
                    matrix[y][x], matrix[nx][nx] = matrix[nx][nx], matrix[y][x]
                    ans = max(ans, get_best()) 
                    matrix[y][x], matrix[nx][nx] = matrix[nx][nx], matrix[y][x] 
    

    
print(ans)
    
