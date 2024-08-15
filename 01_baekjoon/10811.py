import sys
input = sys.stdin.readline

N, M = map(int, input().split())
baguni = [i for i in range(1, N+1)]
baguni = [0] + baguni
temp = []
for _ in range(M):
    i, j = map(int, input().split())
    temp = baguni[i:j+1]
    temp.reverse()
    baguni[i:j+1] = temp

print(' '.join(map(str, baguni[1:])))