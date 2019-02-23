# https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import sys

def geometric(input1, input2):
    ratio = input1[0] / input1[1]
    result = 0
    for non_defect in range(input2):
        result += (((1 - ratio) ** non_defect) * ratio)
    return result

input1 = list(map(int, sys.stdin.readline().rstrip('\n').split()))
input2 = int(sys.stdin.readline().rstrip('\n'))

result = geometric(input1, input2)

sys.stdout.write(str(round(result, 3)))
