import sys

N = int(sys.stdin.readline())

input_string_list = set()
for _ in range(N):
    input_string = sys.stdin.readline().rstrip()
    input_string_list.add(input_string)
    
input_string_list = list(input_string_list)    
input_string_list = sorted(input_string_list, key=lambda each_string: (len(each_string), each_string))

for each_string in input_string_list:
    print(each_string)
    