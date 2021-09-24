import sys

def prime_number(n):
    div = 2
    if n == 1:
        return False
    while(True):
        if div > n**0.5:
            break
        if n % div == 0:
            return False
        div += 1
    return True

while(True):
    input_number = int(sys.stdin.readline())
    if (input_number == 0):
        break
    prime_numbers = []
    end_number = 2*input_number+1
    for request_num in range(input_number, end_number):
        if prime_number(request_num):
            prime_numbers.append(request_num)
    print(len(prime_numbers))


