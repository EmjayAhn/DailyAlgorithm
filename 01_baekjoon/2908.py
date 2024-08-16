import sys
input = sys.stdin.readline

A, B = input().split()
print(max(int(A[::-1]), int(B[::-1])))