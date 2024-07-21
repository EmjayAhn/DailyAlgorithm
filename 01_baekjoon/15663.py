import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

input_number = list(map(int, sys.stdin.readline().split()))
for each_sequence in sorted(set(permutations(input_number, M))):
    print(' '.join(map(str, each_sequence)))
    
