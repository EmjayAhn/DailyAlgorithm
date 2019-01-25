# https://www.acmicpc.net/problem/1924
# 백준 문제 1924
import sys
#
input = sys.stdin.readline().rstrip('\n')
x, y = map(int, input.split())
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
dates = {
    (1, 3, 5, 7, 8, 10, 12): 31,
    (4, 6, 9, 11): 30,
    (2, ): 28
}
total_days = 0
for month in range(1, x):
    for key in list(dates.keys()):
        if month in key:
            total_days += dates[key]
total_days += y
print(days[total_days%7])
