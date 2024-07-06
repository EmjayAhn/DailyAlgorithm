import sys

N = int(sys.stdin.readline().rstrip())
input_list = []
for _ in range(N):
    input_number = int(sys.stdin.readline().rstrip())
    if input_number != 0:
        input_list.append(input_number)
    else:
        input_list.pop()
    
print(sum(input_list))
    
    