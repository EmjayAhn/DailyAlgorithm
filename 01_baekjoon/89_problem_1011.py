t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    c = b - a
    num = 1
    while True:
        if num ** 2 <= c < (num + 1) ** 2:
            break
        num += 1
    if num ** 2 == c:
        print((num * 2) - 1)
    elif num ** 2 < c <= num ** 2 + num:
        print(num * 2)
    else:
        print((num * 2) + 1)
