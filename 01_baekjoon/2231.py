N = int(input())

result = 0
for i in range(N):
    nums = list(map(int, str(i)))
    result = sum(nums) + i
    if result == N:
        print(i)
        break

    if i == N:
        print(0)


