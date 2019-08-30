# https://www.acmicpc.net/problem/2164

import sys

N = int(sys.stdin.readline().rstrip())

deck = [i for i in range(1, N+1)]

while True:
    if len(deck) == 1:
        print(deck[0])
        break
    deck.pop(0)
    deck.append(deck.pop(0))
