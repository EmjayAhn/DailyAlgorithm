import sys
from collections import deque

def dfs(node):
    global adj_list, visited_dfs

    if visited_dfs[node]:
        return
    print(node, end=' ')
    visited_dfs[node] = True
    for adj_node in adj_list[node]:
        dfs(adj_node)
        
def bfs(node):
    global adj_list, visited_bfs
    q = deque()
    q.append(node)
    visited_bfs[node] = True
    print(node, end=' ')
    while q:
    
        node = q.popleft()
        for adj_node in adj_list[node]:
            if not visited_bfs[adj_node]:
                q.append(adj_node)
                visited_bfs[adj_node] = True
                print(adj_node, end=' ') 

N, M, V = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
for _ in range(M):
    node_1, node_2 = map(int, sys.stdin.readline().split())
    adj_list[node_1].append(node_2)
    adj_list[node_2].append(node_1)
for node in range(1, N+1):
    adj_list[node].sort()


dfs(V)
print()
bfs(V)