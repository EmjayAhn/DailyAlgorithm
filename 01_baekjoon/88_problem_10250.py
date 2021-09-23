import sys

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    floor = N % H
    number = N // H + 1
    
    if floor==0:
        floor=H
        number-=1
    room_number = 100*floor + number
    print(room_number)
