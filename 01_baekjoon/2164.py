from collections import deque

def routine(input_list):
    first = input_list.popleft()
    second = input_list.popleft()
    input_list.append(second)
    
N = int(input())
input_list = deque([i for i in range(1, N+1)])

while len(input_list) != 1:
    routine(input_list)
    
print(input_list[0]) 