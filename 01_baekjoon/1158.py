import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())

result = []
input_list = deque([i for i in range(1, N+1)])

while len(input_list) != 0:
    for index in range(K-1):
        move_element = input_list.popleft()
        input_list.append(move_element)
    result.append(input_list.popleft())
    
print("<" + ', '.join(map(str, result)) + ">")