# LCS 에 해당하는 문제
import sys
input = sys.stdin.readline

S1 = input().rstrip()
S2 = input().rstrip()

N, M = len(S1), len(S2)
S1 = " " + S1
S2 = " " + S2
#dp[n][m] : S1의 n 번째 문자까지 살펴보고, S2의 m 번째 문자까지
# 살펴봤을 때 LCS의 길이
#dp[5][6]

DP = [[0] * (M+1) for _ in range(N+1)]

for n in range(1, N+1):
    for m in range(1, M+1):
        if S1[n] == S2[m]:
            DP[n][m] = DP[n-1][m-1] + 1
        if S1[n] != S2[m]:
            DP[n][m] = max(DP[n-1][m], DP[n][m-1])
            

print(DP[N][M])