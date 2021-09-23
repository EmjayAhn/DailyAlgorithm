import sys
input_1 = sys.stdin.readline()
input_2 = sys.stdin.readline()

def solution(input_1, input_2):
    if input_1>0:
        if input_2>0:
            return 1
        elif input_2<0:
            return 4
    else:
        if input_2>0:
            return 2
        else:
            return 3

result = solution(int(input_1), int(input_2))
print(result)

