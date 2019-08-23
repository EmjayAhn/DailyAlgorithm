# https://www.acmicpc.net/problem/4949

import sys

def symmetric(phrase):
    stack = []

    for char in phrase:
        if (char == '(') or (char == '['):
            stack.append(char)

        if char == ')':
            if stack:
                last = stack.pop()
                if last != '(':
                    return 'no'
            else:
                return 'no'
        
        elif char == ']':
            if stack: 
                last = stack.pop()
                if last != '[':
                    return 'no'
            else:
                return 'no'
        
    if stack:
        return 'no'
    else:
        return 'yes'

while True:
    phrase = sys.stdin.readline().rstrip()
    if phrase == '.':
        break
    print(symmetric(phrase))