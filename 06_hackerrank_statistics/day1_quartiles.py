# https://www.hackerrank.com/challenges/s10-quartiles/problem

import sys

def second_quartile(numbers):
    numbers = sorted(numbers)
    if (len(numbers) % 2) == 0:
        median = numbers[len(numbers)//2] + numbers[(len(numbers)//2)-1]
        median = median / 2
    else:
        median = numbers[len(numbers)//2]    
    return round(median)

def first_quartile(numbers, median):
    first = []
    numbers = sorted(numbers)
    for number in numbers:
        if number < median:
            first.append(number)
    return second_quartile(first)

def third_quartile(numbers, median):
    second = []
    numbers = sorted(numbers, reverse=True)
    for number in numbers:
        if number > median:
            second.append(number)
    return second_quartile(second)

number_of_numbers = int(sys.stdin.readline().rstrip('\n'))
numbers = list(map(int, sys.stdin.readline().rstrip('\n').split()))

second = second_quartile(numbers)
first = first_quartile(numbers, second)
third = third_quartile(numbers, second)

sys.stdout.write(str(first) + '\n' + str(second) + '\n' + str(third) + '\n')
