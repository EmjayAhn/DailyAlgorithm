import math
N = int(input())
people = list(map(int, input().split()))
T, P = list(map(int, input().split()))

t_shirt_count = 0
for each_number in people:
    temp = each_number / T
    t_shirt_count += math.ceil(temp)
    
pen_count = (N // P)
pen_remain = (N % P)

print(t_shirt_count)
print(pen_count, end=' ')
print(pen_remain)
