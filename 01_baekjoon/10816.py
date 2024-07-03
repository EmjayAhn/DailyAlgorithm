import sys

N = int(sys.stdin.readline().rstrip())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
M_list = list(map(int, sys.stdin.readline().split()))

count = {}
result = [0 for _ in range(len(M_list))]
for each_number in N_list:
    if not each_number in count:
        count[each_number] = 1
    else:
        count[each_number] += 1
        
for i, each_number in enumerate(M_list):
    try:
        result[i] = count[each_number]
    except:
        result[i] = 0
        
print(' '.join(map(str, result)))