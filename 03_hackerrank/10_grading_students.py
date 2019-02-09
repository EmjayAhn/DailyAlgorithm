# https://www.hackerrank.com/challenges/grading/problem

import sys
import math

def gradingstudents(grades):
    result = []
    for grade in grades:
        compare = (grade // 5 + 1) * 5
        if compare < 40:
            result.append(grade)
        else:
            if (compare - grade) < 3:
                result.append(compare)
            else:
                result.append(grade)
    return result

n = int(sys.stdin.readline().rstrip('\n'))
grades = []
for _ in range(n):
    grade = int(sys.stdin.readline().rstrip('\n'))
    grades.append(grade)
result = gradingstudents(grades)
print('\n'.join(map(str, result)))

