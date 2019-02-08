# https://www.acmicpc.net/board/view/22716
# 백준 문제 22716

import sys
while True:
    try:
        num_inputs = sys.stdin.readline().rstrip('\n')
        for index in range(1, int(num_inputs) + 1):
            inputs = sys.stdin.readline().rstrip('\n')
            A, B = map(int, inputs.split())
            print(A+B)
    except:
        break
