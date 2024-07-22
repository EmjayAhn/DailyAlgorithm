import sys

value = int(sys.stdin.readline().rstrip())
remain = 1000 - value
unit = [500, 100, 50, 10, 5, 1]
count = 0

def change(money, unit):
    coin_count = money // unit
    remain = money % unit
    
    return coin_count, remain

for each_unit in unit:
    coin_count, remain = change(remain, each_unit)
    count += coin_count
    
print(count)
    
