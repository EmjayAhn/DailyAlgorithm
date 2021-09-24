import sys

input_number = int(sys.stdin.readline())

answers = []
i=2
while(True):
    if (input_number == 1):
        break
    if input_number % i == 0:
        answers.append(i)
        input_number = input_number // i
        i=2
    else:
        i+=1

answers.sort()
for element in answers:
    print(element)

