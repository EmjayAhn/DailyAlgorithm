import sys
input = sys.stdin.readline

N = int(input().rstrip())
board = [input().split() for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for j in range(N):
    for i in range(N):
        jump = int(board[j][i])
        
        if jump == 0 or dp[j][i] == 0:
            continue
        if j + jump < N:
            dp[j+jump][i] += dp[j][i]
        if i + jump < N:
            dp[j][i+jump] += dp[j][i]

print(dp[-1][-1])