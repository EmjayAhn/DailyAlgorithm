import sys
input = sys.stdin.readline

input_list = []
default = set([i for i in range(1, 29)])
for _ in range(28):
    input_list.append(int(input()))
input_list = set(input_list)

for each in sorted(list(default - input_list)):
    print(each)