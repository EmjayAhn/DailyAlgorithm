import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())

result_queue = deque()
for _ in range(N):
    input_list = sys.stdin.readline().rstrip().split()
    if input_list[0] == 'push':
        result_queue.append(int(input_list[1]))
    elif input_list[0] == 'pop':
        if len(result_queue) == 0:
            print(-1)
        else:
            popped = result_queue.popleft()
            print(popped)
    elif input_list[0] == 'size':
        print(len(result_queue))
    elif input_list[0] == 'empty':
        if len(result_queue) == 0:
            print(1)
        else:
            print(0)
    elif input_list[0] == 'front':
        if len(result_queue) == 0:
            print(-1)
        else:
            print(result_queue[0])
    else:
        if len(result_queue) == 0:
            print(-1)
        else:
            print(result_queue[-1])

        