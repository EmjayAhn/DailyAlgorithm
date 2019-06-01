# https://www.acmicpc.net/problem/4673

boolean = [True for _ in range(10000)]

def d(n):
    result_sum = n
    while True:
        if n == 0:
            break
        result_sum += n % 10
        n = n // 10
    return result_sum

d_result = [d(number) for number in range(10000)]

for d_num in d_result:
    try:
        boolean[d_num-1] = False
    except:
        continue
for index, bool_ in enumerate(boolean):
    if bool_:
        print(index + 1)






