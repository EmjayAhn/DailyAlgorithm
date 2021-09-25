import sys

def fibonacci(number):
    if (number == 0) or (number == 1):
        return number
    else:
        number = fibonacci(number-1) + fibonacci(number-2)
        return number

input_number = int(sys.stdin.readline())

print(fibonacci(input_number))
    