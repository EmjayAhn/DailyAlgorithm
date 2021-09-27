import sys
N = int(sys.stdin.readline())

input_list = []
for _ in range(N):
    input_number = int(sys.stdin.readline())
    input_list.append(input_number)

# 산술평균
mean = round(sum(input_list) / len(input_list))

# 중앙값
sorted_list = sorted(input_list)
median = sorted_list[len(input_list)//2]

#최빈값
count = {}
for data in sorted_list:
    if data not in count:
        count[data] = 1
    else:
        count[data] += 1

mode = max(count.keys(), key=lambda k: (count[k], list(count.keys())))

#범위
range_val = sorted_list[N-1] - sorted_list[0]


print(mean)
print(median)
print(mode)
print(range_val)

