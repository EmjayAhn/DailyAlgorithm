import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chess = []
for _ in range(N):
    chess.append(input())
    