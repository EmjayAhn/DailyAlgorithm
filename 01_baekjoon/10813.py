import sys
input = sys.stdin.readline

N, M = map(int, input().split())
baguni = [i for i in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    baguni[i], baguni[j] = baguni[j], baguni[i]

print(' '.join(map(str, baguni[1:])))
