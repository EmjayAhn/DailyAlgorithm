# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import sys

def geometric(input1, input2):
    ratio = input1[0] / input1[1]
    result = ((1 - ratio) ** (input2 - 1)) * ratio
    return result

input1 = list(map(int, sys.stdin.readline().rstrip('\n').split()))
input2 = int(sys.stdin.readline().rstrip('\n'))

result = geometric(input1, input2)

sys.stdout.write(str(round(result, 3)))
