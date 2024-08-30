import sys
import string
input = sys.stdin.readline

N, B = input().split()
B = int(B)

result = 0
alphabet = string.ascii_uppercase
for index, each_character in enumerate(N[::-1]):
    if each_character in alphabet:
        number = (10 + alphabet.index(each_character))
    else:
        number = int(each_character)
    
    result += (number * (B ** index))
print(result)
       