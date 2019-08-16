# # https://www.acmicpc.net/problem/1107

import sys

target_channel = sys.stdin.readline().rstrip()
num_broken = int(sys.stdin.readline().rstrip())
broken_buttons = list(map(int, sys.stdin.readline().rstrip().split()))

buttons_able = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if num_broken !=0 :
    for broken in broken_buttons:
        buttons_able.remove(broken)

result = abs(int(target_channel) - 100)
for cur_channel in range(1000001):
    enable = True
    for char in str(cur_channel):
        if int(char) not in buttons_able:
            enable = False
    if enable:
        result = min(result, abs(cur_channel - int(target_channel)) + len(str(cur_channel)))



print(result)        

# def current_channel(target_channel, num_broken, broken_buttons):
#     if num_broken !=0 :
#         for broken in broken_buttons:
#             buttons_able.remove(broken)

#     cur_number = ''
#     for str_number in target_channel:
#         cur = ''
#         min_difference = 10
#         for button_able in buttons_able:
#             difference = abs(button_able - int(str_number))
#             if difference < min_difference:
#                 min_difference = difference
#                 cur = str(button_able)
#         cur_number += cur
    
#     return cur_number

# def main(target_channel, num_broken, broken_buttons):
#     result = []
#     cur_number = current_channel(target_channel, num_broken, broken_buttons)
#     result.append(abs(int(target_channel) - int(cur_number)) + len(str(cur_number)))

#     result.append(abs(int(target_channel) - 100))
#     return min(result)

# print(main(target_channel, num_broken, broken_buttons))
