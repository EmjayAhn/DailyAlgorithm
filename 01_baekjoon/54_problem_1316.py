# https://www.acmicpc.net/problem/1316

import sys

N = int(sys.stdin.readline().rstrip('\n'))
count = 0

def check_group_word(word):
    char_dict = {}
    result = []
    for index, char in enumerate(word):
        try:
            char_dict[char].append(index)
        except:
            char_dict[char] = [index]
    
    for value in char_dict.values():
        value = sorted(value)
        if value[0] + len(value) - 1 == value[-1]:
            result.append(True)
        else:
            result.append(False)
    return all(result)

for _ in range(N):
    input_word = sys.stdin.readline().rstrip('\n')
    result = check_group_word(input_word)
    if result:
        count += 1
print(count)