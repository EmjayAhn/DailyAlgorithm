import sys

def dfs(node):
    global adj_list, visited
     
    if visited[node]:
        return
    
    visited[node] = True
    for adj_node in adj_list[node]:
        dfs(adj_node)

N, M = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)
    
for each_node in range(1, N+1):
    if not visited[each_node]:
        dfs(each_node)
        count += 1
        
print(count)
    


    