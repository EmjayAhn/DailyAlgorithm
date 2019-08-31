# https://www.acmicpc.net/problem/2588

m = input()
n = input()

for number in n[::-1]:
    result = int(m) * int(number)
    print(result)

print(int(m)*int(n))
