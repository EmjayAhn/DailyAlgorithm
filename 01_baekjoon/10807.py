import sys
input = sys.stdin.readline

N = int(input())
input_list = list(map(int, input().split()))
v = int(input())

count = 0
for i in input_list:
    if v == i:
        count += 1
print(count)