import sys
input = sys.stdin.readline

input_string = input()

if input_string == input_string[::-1]:
    print(1)
else:
    print(0)