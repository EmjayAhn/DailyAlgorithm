# https://www.hackerrank.com/challenges/s10-standard-deviation/problem?h_r=next-challenge&h_v=zen

import sys

def std(numbers):
    mean = sum(numbers) / len(numbers)
    nums_eliminate_mean = [(number - mean)**2 for number in numbers]
    variance = sum(nums_eliminate_mean) / len(nums_eliminate_mean)
    std = variance ** 0.5
    return std

number_of_numbers = int(sys.stdin.readline().rstrip('\n'))
numbers = list(map(int, sys.stdin.readline().rstrip('\n').split()))

standard_deviation = round(std(numbers), 1)
sys.stdout.write(str(standard_deviation) + '\n')

