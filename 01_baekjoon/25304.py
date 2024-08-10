import sys
input = sys.stdin.readline

X = int(input())

N = int(input())
total_price = 0
for _ in range(N):
    price, amount = map(int, input().split())
    total_price += (price * amount)
    
if total_price == X:
    print("Yes")
else:
    print("No")

    