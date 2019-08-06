# https://www.acmicpc.net/problem/1003

memory0 = {0: 1, 1: 0, 2: 1}
memory1 = {0: 0, 1: 1, 2: 1}

def how_much_call(num):
    if num not in memory0:
        for i in range(3, num+1):
            memory0[i] = memory0[i-2] + memory0[i-1]
            memory1[i] = memory1[i-2] + memory1[i-1]

    return memory0[num], memory1[num]


num_iter = int(input())

for _ in range(num_iter):
    N = int(input())
    result = how_much_call(N)
    print("{} {}".format(result[0], result[1]))
