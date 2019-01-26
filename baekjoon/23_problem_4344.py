# https://www.acmicpc.net/problem/4344
# 백준 문제 4344
import sys

input1 = sys.stdin.readline().rstrip('\n')

for _ in range(int(input1)):
    input2 = sys.stdin.readline().rstrip('\n')
    input2 = list(map(int, input2.split()))
    scores = input2[1:]
    num_students = input2[0]
    average = sum(scores) / num_students
    count = 0
    for score in scores:
        if score > average:
            count += 1
    print('{0:.3f}%'.format(count/num_students*100))
