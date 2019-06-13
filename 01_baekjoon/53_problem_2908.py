# https://www.acmicpc.net/problem/2908

import sys

input_numbers = sys.stdin.readline().rstrip('\n').split()

input_number1 = input_numbers[0][::-1]
input_number2 = input_numbers[1][::-1]

print(max(input_number1, input_number2))