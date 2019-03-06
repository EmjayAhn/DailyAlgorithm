# https://www.hackerrank.com/challenges/30-nested-logic/problem

import sys

def cal_fine(due_date, actual_date):
    fine = 0
    if due_date[2] == actual_date[2]:
        if due_date[1] == actual_date[1]:
            if due_date[0] >= actual_date[0]:
                fine = 0
            else:
                fine = 15 * (actual_date[0] - due_date[1])
        elif due_date[1] > actual_date[1]:
            fine = 0
        else:
            fine = 500 * (actual_date[1] - due_date[1])
    elif due_date[2] > actual_date[2]:
        fine = 0
    else:
        fine = 10000
    return fine

actual_date = list(map(int, sys.stdin.readline().rstrip('\n').split()))
due_date = list(map(int, sys.stdin.readline().rstrip('\n').split()))

result = cal_fine(due_date, actual_date)
sys.stdout.write(str(result))
