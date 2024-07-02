import sys

N = int(sys.stdin.readline())

input_list = []
for _ in range(N):
    input_list.append(sys.stdin.readline().split())
    
input_list = sorted(input_list, key=lambda each_list: (int(each_list[0])))
for each_list in input_list:
    print(' '.join(each_list))
