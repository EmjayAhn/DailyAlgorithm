# https://www.acmicpc.net/problem/1110

import sys

def augment(number):
    number = str(number)
    assert len(number) == 1
    return '0' + number

input = sys.stdin.readline().rstrip('\n')

iteration = 1
cur_number = input
while True:
    if len(cur_number) == 1:
        cur_number = augment(cur_number)
    
    calculated_number = str(int(cur_number[0]) + int(cur_number[1]))
    
    if len(calculated_number) == 1:
        calculated_number = augment(calculated_number)

    new_number = cur_number[1] + calculated_number[1]

    if int(new_number) == int(input):
        print(iteration)
        break
    cur_number = new_number
    iteration += 1