import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split())) 

sum = 0
for _ in range(len(B)):
    max_value = max(B)
    min_value = min(A)
    sum += (max_value * min_value)
    
    max_value_index = B.index(max_value)
    min_value_index = A.index(min_value)
    del B[max_value_index]
    del A[min_value_index]
    
print(sum)