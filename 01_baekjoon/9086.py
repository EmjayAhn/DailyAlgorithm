import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    input_string = input().rstrip()
    print(input_string[0]+input_string[-1])