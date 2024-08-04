import sys
input = sys.stdin.readline

N = int(input())
warehouse = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
dp[1] = warehouse[1]

for i in range(2, N+1):
    dp[i] = max(dp[i-1], dp[i-2] + warehouse[i])
    
print(max(dp))



