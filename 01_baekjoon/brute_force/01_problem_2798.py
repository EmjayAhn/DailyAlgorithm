# https://www.acmicpc.net/problem/2798

import sys

N, M = list(map(int, sys.stdin.readline().rstrip().split()))
cards = list(map(int, sys.stdin.readline().rstrip().split()))

def black_jack(N, M, cards):
    max_sum = 0
    total_sum = 0

    for first_index, _ in enumerate(cards[:-2]):
        second_count = 0
        second_index = first_index
        while second_index < N - 1:
            second_count += 1
            second_index = first_index + second_count

            third_count = 0
            third_index = second_index
            while third_index < N-1:
                third_count += 1
                third_index = second_index + third_count

                total_sum = cards[first_index] + cards[second_index] + cards[third_index]
                if (total_sum > max_sum) and (total_sum <= M):
                    max_sum = total_sum
    return max_sum

print(black_jack(N, M, cards))



