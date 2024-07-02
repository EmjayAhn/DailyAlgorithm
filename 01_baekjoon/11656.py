import sys
input_string = sys.stdin.readline().rstrip()
input_length = len(input_string)
array = []
for i in range(input_length):
    array.append(input_string[i:])

for each_string in sorted(array):
    print(each_string)