import sys

input_number = int(sys.stdin.readline())

standard = 1
i = 1
while(True):
    if input_number <= standard:
        break
    standard += 6*i
    i+=1

print(i)
