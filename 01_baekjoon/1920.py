import sys

N = int(input())
A = list(map(int, input().split()))
M = int(input())
M = list(map(int, input().split()))
    
# A = set(map(int, input().split()))
# for each_m_number in M:
#     print(int(each_m_number in A))
 
 # 이분탐색을 이용해 다시 짜보면,
 
A = sorted(A)
 
 
for target in M:
    left_index = 0
    right_index = N-1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        
        if target > A[mid_index]:
            left_index = mid_index + 1
        if target < A[mid_index]:
            right_index = mid_index - 1
        if target == A[mid_index]:
            print(1)
            break

    if target != A[mid_index]:
        print(0)
    
    
     
     