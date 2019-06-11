# https://www.acmicpc.net/problem/2920

import sys

input_ = sys.stdin.readline().rstrip('\n')
input_ = list(map(int, input_.split()))

if input_ == [1, 2, 3, 4, 5, 6, 7, 8]:
    print("ascending")
elif input_ == [8, 7, 6, 5, 4, 3, 2, 1]:
    print('descending')
else:
    print("mixed")

    
    