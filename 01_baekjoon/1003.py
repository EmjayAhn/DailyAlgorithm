import sys
input = sys.stdin.readline
def fibo(n):
    global count_0, count_1
    if n == 0:
        count_0 += 1
        return 0
    elif n == 1:
        count_1 += 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
T = int(input())
for _ in range(T):
    count_0 = 0
    count_1 = 0

    N = int(input())
    fibo(N)
    print(count_0, count_1)