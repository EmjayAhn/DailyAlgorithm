import sys
from collections import deque
MAX = int(1e5)
N, K = map(int, sys.stdin.readline().split())

q = deque()
visited = [False] * (MAX + 1)

q.append((0, N))
visited[N] = True

while q:
    time, position = q.popleft()
    
    if position == K:
        print(time)
        exit()
    
    for next_position in [position-1, position+1, 2 * position]:
        if (0 <= next_position <= MAX) and (not visited[next_position]):
            q.append((time + 1, next_position))
            visited[next_position] = True


