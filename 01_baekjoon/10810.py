import sys
input = sys.stdin.readline

N, M = map(int, input().split())
baguni = [0] * (N+1)
for _ in range(M):
    i, j, k = map(int, input().split())
    baguni[i:j+1] = [k] * (j - i + 1)
    
print(' '.join(map(str, baguni[1:])))
    