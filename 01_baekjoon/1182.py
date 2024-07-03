import sys
from itertools import combinations
N, S = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))


def sum_of_combinations(n, count, S):
    for each_combination in combinations(array, n):
        sum_each_combination = sum(each_combination)
        if sum_each_combination == S:
            count += 1            
    return count

count = 0
for n in range(1, N+1):
    count = sum_of_combinations(n, count, S)
    
print(count)

