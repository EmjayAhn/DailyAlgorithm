import sys
input = sys.stdin.readline

input_list = []
for _ in range(9):
    input_list.append(list(map(int, input().split())))
    
max_index = 0
max_jndex = 0
max_value = 0
for i in range(9):
    temp = max(input_list[i])
    if temp > max_value:
        max_value = temp
        max_index = i
        max_jndex = input_list[i].index(temp)

print(max_value)
print(max_index+1, max_jndex+1)
        