# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import sys

def birthdaycakecandles(ar):
    index = 0
    array = sorted(ar, reverse=True)
    while index < len(array)-1:
        if (array[index] != array[index+1]):
            break
        index += 1
    return index + 1

num_candles = int(sys.stdin.readline().rstrip('\n'))
candles = list(map(int, sys.stdin.readline().rstrip('\n').split()))
result = birthdaycakecandles(candles)
print(result)