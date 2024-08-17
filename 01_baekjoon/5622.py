import sys
input = sys.stdin.readline

input_string = input().rstrip()

str2num = {
    'ABC': 2,
    'DEF': 3,
    'GHI': 4,
    'JKL': 5,
    'MNO': 6,
    'PQRS': 7,
    'TUV': 8,
    'WXYZ': 9
}

def find_keys(string):
    for each in list(str2num.keys()):
        if string in each:
            return each

result = 0
for each_string in input_string:
    key = find_keys(each_string)
    result += (str2num[key] + 1)
    
print(result)