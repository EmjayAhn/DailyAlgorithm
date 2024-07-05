import sys

N = int(sys.stdin.readline())

count = 1
current_number = 666
while True:
    if count == N:
        break
    current_number += 1
    if '666' in str(current_number):
        count += 1
    
print(current_number)
    
    