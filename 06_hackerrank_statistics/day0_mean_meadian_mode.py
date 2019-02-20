# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

import sys

def mean(numbers, number_of_numbers):
    return sum(numbers) / number_of_numbers
    
def median(numbers, number_of_numbers):
    numbers = sorted(numbers)
    if (number_of_numbers % 2) == 0:
        median = numbers[number_of_numbers//2] + numbers[(number_of_numbers//2)-1]
        median = median / 2
    else:
        median = numbers[number_of_numbers//2]
    return median

def mode(numbers):
    count_dict = {}
    for number in numbers:
        try:
            count_dict[number] += 1
        except:
            count_dict[number] = 1
    sort_dict = sorted(count_dict.items(), key=lambda items: (-items[1], items[0]))
    return sort_dict[0][0]

number_of_numbers = int(sys.stdin.readline().rstrip('\n'))
numbers = list(map(int, sys.stdin.readline().rstrip('\n').split()))

mean = mean(numbers, number_of_numbers)
median = median(numbers, number_of_numbers)
mode = mode(numbers)

sys.stdout.write(str(mean) + '\n' + str(median) + '\n' + str(mode) + '\n')


