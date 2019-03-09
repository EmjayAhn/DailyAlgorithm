# https://www.hackerrank.com/challenges/30-bitwise-and/problem

def max_bitwise(n, k):
    max_bitwise = 0
    for i in range(1, n+1):
        for j in range(1, i):
            bitwise = i & j
            if max_bitwise < bitwise < k:
                max_bitwise = bitwise
                if max_bitwise == k - 1:
                    return max_bitwise
    return max_bitwise
t = int(input())
for t_itr in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    print(max_bitwise(n, k))