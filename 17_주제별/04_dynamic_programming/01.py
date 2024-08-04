"""
문제 :정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이
4가지 이다.

    1. X가 5로 나누어떨어지면, 5로 나눈다.
    2. X가 3으로 나누어 떨어지면, 3으로 나눈다.
    3. X가 2로 나누어떨어지면, 2로 나눈다.
    4. X에서 1을 뺀다.

정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만들려고 한다. 연산을
사용하는 횟수의 최솟값을 출력하시오.

dp[n] : n이 1이 되는 연산의 최소 수 
dp[1] : 1이 1이 되는 연산의 최소 수  -> 0개
"""

import sys
input = sys.stdin.readline

X = int(input())
dp = [0] * 30001

for i in range(2, X+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    elif i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    elif i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5]+1)
print(dp[:5])
print(dp[X])