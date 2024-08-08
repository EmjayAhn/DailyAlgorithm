import sys
input = sys.stdin.readline

input_list = list(map(int, input().split()))
count_array = [0] * 7
for i in input_list:
    count_array[i] += 1

if 3 in count_array:
    value = count_array.index(3)
    print(10000 + value * 1000)
elif 2 in count_array:
    value = count_array.index(2)
    print(1000 + value * 100)
else:
    max_ = 0
    for index, value in enumerate(count_array):
        if value == 1:
            max_ = max(index, max_)
    print(max_*100)
            

        