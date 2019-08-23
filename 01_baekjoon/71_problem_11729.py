# https://www.acmicpc.net/problem/11729

N = int(input())

# count = 0

# def hanoi_count(N):
#     global count
#     if N == 1:
#         count = 1
#         return count
#     count = 2 * hanoi_count(N-1) + 1
#     return count

def hanoi_count(N):
    if N == 1:
        return 1
    return 2 * hanoi_count(N-1) + 1

def hanoi_movement(N, start, dest):
    if N == 1:
        print("{} {}".format(start, dest))
    else:
        hanoi_movement(N-1, 1, 2)
        hanoi_movement(1, 1, 3)
        hanoi_movement(N-1, 2, 3)

    

print(hanoi_count(N))
hanoi_movement(N, 1, 3)