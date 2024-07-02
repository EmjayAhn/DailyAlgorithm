import sys

N = int(input())
A = set(map(int, input().split()))
M = int(input())
M = list(map(int, input().split()))
    

for each_m_number in M:
    print(int(each_m_number in A))