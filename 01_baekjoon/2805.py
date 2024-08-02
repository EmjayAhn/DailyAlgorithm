N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) 

while start <= end: 
    mid = (start+end) // 2
    
    log = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid
    
    #벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)