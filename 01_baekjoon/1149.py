import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [[0] + list(map(int, input().split())) for _ in range(N)]
arr = [[0] * (4)] + arr
dp = [[0, 0, 0, 0] for _ in range(N+1)]    
# dp(i, j) = min(dp(i-1, j가 아닌 index)) + arr[i, j]

dp[1][1] = arr[1][1]
dp[1][2] = arr[1][2] 
dp[1][3] = arr[1][3]
for i in range(2, N+1):
    for j in range(1, 4):
        if j == 1:
            dp[i][j] = arr[i][1] + min(dp[i-1][2], dp[i-1][3])
        elif j == 2:
            dp[i][j] = arr[i][2] + min(dp[i-1][1], dp[i-1][3])
        else:
            dp[i][j] = arr[i][3] + min(dp[i-1][1], dp[i-1][2])

print(min(dp[N][1:4]))


