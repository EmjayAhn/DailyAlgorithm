import sys


while(True):
    inputs = sys.stdin.readline()
    inputs = list(map(int, inputs.split()))
    if inputs == [0, 0, 0]:
        break
    long = max(inputs)
    inputs.pop(inputs.index(long))
    a, b = inputs
    if (long**2  == (a**2 + b**2)):
        print("right")
    else:
        print("wrong")

