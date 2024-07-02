import sys

N = int(sys.stdin.readline())
input_list = []

for _ in range(N):
    input_list.append(list(map(int, sys.stdin.readline().split())))
    
input_list = sorted(input_list, key=lambda each_element: (each_element[1]*each_element[2]*each_element[3], each_element[1]+each_element[2]+each_element[3], each_element[0]))

print(input_list[0][0], input_list[1][0], input_list[2][0])