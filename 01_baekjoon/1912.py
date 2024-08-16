# input
N = int(input())
arr = [0] + list(map(int, input().split()))

# solve
dp = [0 for _ in range(N + 1)]

for n in range(1, N + 1):
    dp[n] = max(dp[n - 1], 0) + arr[n]

print(max(dp[1:]))
