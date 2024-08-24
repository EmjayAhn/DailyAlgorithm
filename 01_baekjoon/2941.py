import sys
input = sys.stdin.readline
input_string = input()
alphabet_list = [
    'c=',
    'c-',
    'dz=',
    'd-',
    'lj',
    'nj',
    's=',
    'z='
]

for i in alphabet_list:
    input_string = input_string.replace(i, '*')

print(len(input_string))
    