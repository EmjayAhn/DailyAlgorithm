import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())

result = []
input_list = deque([i for i in range(1, N+1)])

while len(input_list) != 0:
    # [1, 2, 3, 4, 5, 6, 7]
    for _ in range(K-1):
        input_list.append(input_list.popleft())
    
    result.append(input_list.popleft())

print('<' + ', '.join(map(str, result)) + '>')
    
    