import sys

N = int(sys.stdin.readline())

input_list = []
for _ in range(N):
    input_number = int(sys.stdin.readline())
    input_list.append(input_number)
    
for each_number in sorted(input_list):
    print(each_number)
    