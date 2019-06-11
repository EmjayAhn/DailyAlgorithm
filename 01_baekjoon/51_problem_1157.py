# https://www.acmicpc.net/problem/1157

import sys

input_string = sys.stdin.readline().rstrip('\n').lower()

results = {}
result = '?'

for char in input_string:
    try:
        results[char] += 1
    except:
        results[char] = 1
sort = sorted(results.items(), key=lambda item: -item[1])
if len(sort) > 1:
    if sort[0][1] == sort[1][1]:
        result = '?'
    else:
        result = sort[0][0].upper()
else:
    result = input_string.upper()
print(result)