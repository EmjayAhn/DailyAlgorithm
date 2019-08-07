# https://www.acmicpc.net/problem/1193

import sys

Nth = int(sys.stdin.readline().rstrip())
n = 0
starting_point = 1
end_point = 1
result = None

while True:
    if (starting_point <= Nth) and (end_point >= Nth):
        result = n + 1
        break
    n += 1
    starting_point = starting_point + n
    end_point = end_point + n + 1

if result % 2 == 0:
    print(str(int(Nth - starting_point + 1)) + '/' + str(result - Nth + starting_point))
else:
    print(str(result - Nth + starting_point) + '/' + str(int(Nth - starting_point + 1)))