import sys

def factorial(N):
    #escape condition
    if (N == 0) or (N == 1):
        return 1
    return N * factorial(N-1)

input_number = int(sys.stdin.readline())

answer = factorial(input_number)
print(answer)