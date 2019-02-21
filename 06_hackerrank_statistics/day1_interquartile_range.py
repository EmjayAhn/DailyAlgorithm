# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

import sys

def second_quartile(numbers):
    numbers = sorted(numbers)
    if (len(numbers) % 2) == 0:
        median = numbers[len(numbers)//2] + numbers[(len(numbers)//2)-1]
        median = median / 2
    else:
        median = numbers[len(numbers)//2]    
    return median

def first_quartile(numbers):
    numbers = sorted(numbers)
    half = len(numbers) // 2
    return second_quartile(numbers[:half])

def third_quartile(numbers):
    numbers = sorted(numbers)
    half = len(numbers) // 2
    if (len(numbers) % 2) == 0:
        return second_quartile(numbers[half:])
    else:
        return second_quartile(numbers[half+1:])

def interquartile_range(numbers):
    return (third_quartile(numbers) - first_quartile(numbers))

number_of_numbers = int(sys.stdin.readline().rstrip('\n'))
input_numbers = list(map(int, sys.stdin.readline().rstrip('\n').split()))
frequency = list(map(int, sys.stdin.readline().rstrip('\n').split()))    

numbers = [number for index, number in enumerate(input_numbers) for _ in range(frequency[index])]
result = round(float(interquartile_range(numbers)), 2)

sys.stdout.write(str(result) + '\n')
