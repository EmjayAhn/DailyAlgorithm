import sys
from itertools import permutations

input_number = sys.stdin.readline().rstrip()
number_list = []
for each_number in list(permutations(input_number)):
    number_list.append(int(''.join(each_number)))
    
number_list = sorted(number_list)
for each_number in number_list:
    if each_number > int(input_number):
        print(each_number)
        break