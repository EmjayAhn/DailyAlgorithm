import sys

def hanoi(N, a, b, c):
    #escape condition
    if N == 1:
        move.append([a, c])
        return 1
    hanoi(N-1, a, c, b)
    move.append([a, c])
    hanoi(N-1, b, a, c)

move = []
input_number = int(sys.stdin.readline())
hanoi(input_number, 1, 2, 3)


print(len(move))
print("\n".join([' '.join(str(i) for i in row) for row in move]))
