import math

N = int(input())
input_list = list(map(int, input().split()))
count = 0

def check_primenumber(number):
    result = []
    if number == 1:
        return False

    for i in range(1, int(math.sqrt(number)) +1) :
        if number % i == 0:
            result.append(i)
    return True if len(result) == 1 else False
        
        
for each_number in input_list:
    if check_primenumber(each_number):
        count += 1
    
print(count)