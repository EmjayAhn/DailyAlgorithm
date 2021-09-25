import sys

input_number = int(sys.stdin.readline())
list_number = []
answer = ''

for each in str(input_number):
    list_number.append(each)

sorted_list_number = sorted(list_number, reverse=True)

for each in sorted_list_number:
    answer += str(each)

print(answer)