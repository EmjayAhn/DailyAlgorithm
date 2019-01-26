# https://www.acmicpc.net/problem/10809
# 백준 문제 10809
import sys
import string

input = sys.stdin.readline().rstrip('\n')
alphabets = string.ascii_lowercase
result = ''
for alphabet in alphabets:
    try:
        result += str(input.index(alphabet))
        result += ' '
    except:
        result += '-1'
        result += ' '
print(result)
