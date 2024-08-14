import sys
input = sys.stdin.readline

N = int(input())
input_list = list(map(int, input().split()))

value = -1000
for i in range(N):
    for j in range(i+1, N+1):
        cur_sum = sum(input_list[i:j])
        value = max(cur_sum, value)
        
print(value)
    