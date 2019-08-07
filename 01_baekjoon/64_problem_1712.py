# https://www.acmicpc.net/problem/1712

import sys
import math

def cal_breakpoint(A, B, C):
    if (C - B) <= 0:
        return -1
    else:
        return (A // (C - B)) + 1
        
inputs = sys.stdin.readline().rstrip()
inputs = list(map(int, inputs.split()))
A = inputs[0]
B = inputs[1]
C = inputs[2]

result = cal_breakpoint(A, B, C)
print(result)
