# https://www.acmicpc.net/problem/9012

import sys

T = int(sys.stdin.readline().rstrip())

def find_VPS(paranthesis):
    stack = []
    for char in paranthesis:
        if char == "(":
            stack.append(char)
        else:
            try:
                stack.pop()
            except:
                return "NO"

    if len(stack) != 0:
        return "NO"
    else:
        return "YES"

for _ in range(T):
    paranthesis = sys.stdin.readline().rstrip()
    print(find_VPS(paranthesis))
                