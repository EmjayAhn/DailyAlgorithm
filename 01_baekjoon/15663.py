import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

input_number = list(map(int, sys.stdin.readline().split()))
for each_sequence in sorted(set(permutations(input_number, M))):
    print(' '.join(map(str, each_sequence)))
    
## 다른 풀이
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return
    remember_me = 0
    for i in range(n):
        if not visited[i] and remember_me != nums[i]:
            visited[i] = True
            temp.append(nums[i])
            remember_me = nums[i]
            dfs()
            visited[i] = False
            temp.pop()

dfs()