# https://www.acmicpc.net/problem/2588

import sys
N1 = int(sys.stdin.readline().rstrip('\n'))
N2 = sys.stdin.readline().rstrip('\n')

step1 = N1 * int(N2[2])
step2 = N1 * int(N2[1])
step3 = N1 * int(N2[0])

print(step1)
print(step2)
print(step3)
print(step1 + step2 * 10 + step3 * 100)


