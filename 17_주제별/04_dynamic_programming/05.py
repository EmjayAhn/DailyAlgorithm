import sys
input = sys.stdin.readline

N, M = map(int, input().split())
coins = []
dp = [0] + [10001] * 10000
for _ in range(N):
    k = int(input())
    coins.append(k)
    dp[k] = 1
    
    
for i in range(2, M+1):
    for k in coins:
        dp[i] = min(dp[i], dp[i-k]+1)
        
if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])
    
    