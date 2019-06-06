# https://www.acmicpc.net/problem/8958

import sys

def calculate_score(OX_strings):
    transfer_list = []
    for string in OX_strings:
        if string == 'O':
            transfer_list.append(1)
        elif string == 'X':
            transfer_list.append(0)
    
    score_list = []
    for index, score in enumerate(transfer_list):
        if score == 1:
            try:
                cur_score = score_list[index-1] + 1
            except:
                cur_score = 1
            score_list.append(cur_score)
        if score == 0:
            score_list.append(0)
    final_result = sum(score_list)
    return final_result


N = int(sys.stdin.readline().rstrip('\n'))

for _ in range(N):
    OX_strings = sys.stdin.readline().rstrip('\n')
    print(calculate_score(OX_strings))
