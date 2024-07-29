import sys
INFINITE = sys.maxsize
N = int(sys.stdin.readline().rstrip())
blocks = sys.stdin.readline()

dp = [INFINITE] * N
dp[0] = 0

for i in range(1, N):
    for j in range(i):
        if blocks[i] == 'B' and blocks[j] == 'J':
            dp[i] = min(dp[i], dp[j]+(i-j)**2)
        elif blocks[i] == 'O' and blocks[j] == 'B':
            dp[i] = min(dp[i], dp[j]+(i-j)**2)
        elif blocks[i] == 'J' and blocks[j] == 'O':
            dp[i] = min(dp[i], dp[j]+(i-j)**2)

if dp[N-1] == INFINITE:
    print(-1)
else:
    print(dp[N-1])