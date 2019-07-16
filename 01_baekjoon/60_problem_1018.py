# https://www.acmicpc.net/problem/1018

import sys

n_row, n_column = map(int, sys.stdin.readline().rstrip().split())

origin_board = []
final_result = 9e20

for _ in range(n_row):
    origin_board.append(sys.stdin.readline().rstrip())

def check_min_num(start_point):
    
    change_white = 0
    change_black = 0

    # start with white marker
    for index_row, start_row in enumerate(range(start_point[0], start_point[0]+8)):
        for index_column, start_column in enumerate(range(start_point[1], start_point[1] + 8)):
            if (index_column % 2) == 0:
                if ((index_row % 2) == 0) & (origin_board[start_row][start_column]=='B'):
                    change_white += 1
                if ((index_row % 2) == 1) & (origin_board[start_row][start_column]=='W'):
                    change_white += 1
            else:
                if ((index_row % 2) == 0) & (origin_board[start_row][start_column]=='W'):
                    change_white += 1
                if ((index_row % 2) == 1) & (origin_board[start_row][start_column]=='B'):
                    change_white += 1

    for index_row, start_row in enumerate(range(start_point[0], start_point[0]+8)):
        for index_column, start_column in enumerate(range(start_point[1], start_point[1] + 8)):
            if (index_column % 2) == 0:
                if ((index_row % 2) == 0) & (origin_board[start_row][start_column]=='W'):
                    change_black += 1
                if ((index_row % 2) == 1) & (origin_board[start_row][start_column]=='B'):
                    change_black += 1
            else:
                if ((index_row % 2) == 0) & (origin_board[start_row][start_column]=='B'):
                    change_black += 1
                if ((index_row % 2) == 1) & (origin_board[start_row][start_column]=='W'):
                    change_black += 1

    return min(change_white, change_black)           


for start_row in range(n_row-7):
    for start_col in range(n_column-7):
        result = check_min_num([start_row, start_col])
        final_result = min(final_result, result)

print(final_result)

    

            






        




