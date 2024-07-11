from collections import deque
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    importance = deque(map(int, input().split()))
    
    result = 1
    while importance:
        if importance[0] < max(importance):
            importance.append(importance.popleft())
            
        else:
            if m == 0:
                break
            importance.popleft()
            result += 1
            
        if m > 0:
            m -= 1
        else:
            m = len(importance) - 1
            
    print(result)
            
            