# https://www.acmicpc.net/problem/1152
import sys

input = sys.stdin.readline().rstrip('\n')

words = input.split(' ')

if words[0] == '':
    words.pop(0)
if words[-1] == '':
    words.pop(-1)
print(len(words))