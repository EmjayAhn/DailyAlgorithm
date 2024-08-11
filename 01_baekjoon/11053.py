# LIS (Longest increasing Subsequence) 문제
"""
DP table 설계
dp[n] : n 번째까지 살펴보았을 때의 LIS
dp[n] = dp[n-1] 이렇게 정의하면 dp[n-1] 의 마지막 값을 몰라 n 번째 원소가 들어갈지
안들어갈지 모름

dp[n] : n에서 끝나는 LIS의 길이
따라서 답은 max(dp[1], dp[2], dp[3], dp[4] ... dp[n])


"""
import sys


input = sys.stdin.readline
N = int(input().rstrip())
A = [0] + list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = 1
for n in range(2, N+1):
    best = 0
    for i in range(1, n):
        if A[n] > A[i]:
            best = max(best, dp[i])
    dp[n] = best + 1
         
        
print(max(dp[1:]))