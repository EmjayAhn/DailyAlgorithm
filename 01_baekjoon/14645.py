N, K = map(int, input().split())

count = K
for _ in range(N):
    A, B = map(int, input().split())
    K = K + A - B
    
    