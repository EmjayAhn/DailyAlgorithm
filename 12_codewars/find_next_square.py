# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python
import sys
def find_next_square(sq):
    sqrt = round(sq**(1/2), 1)
    if sqrt**2 == sq:
        testing_number = sq + 1
        while True:
            if round(testing_number**(1/2), 1) ** 2 == testing_number:
                break
            else:
                testing_number += 1 
        return testing_number

    else:
        return -1

input_number = int(sys.stdin.readline())
print(find_next_square(input_number))
