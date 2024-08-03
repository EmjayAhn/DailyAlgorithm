import sys
input = sys.stdin.readline
K, N = map(int, input().split())
K_list = []
for _ in range(K):
    K_list.append(int(input().rstrip()))
    
start, end = 1, max(K_list)
reuslt = 0
while start <= end:
    mid = (start + end) // 2
    line_count = 0
    for i in K_list:
        line_count += i // mid
    
    if line_count >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
    