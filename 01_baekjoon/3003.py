import sys
input = sys.stdin.readline

# king 1, queen 1, look 2, knight, 2, pone 8
exact_king = 1
exact_queen = 1
exact_look = 2
exact_bishop = 2
exact_knight = 2
exact_pone = 8

king, queen, look, bishop, knight, pone = map(int, input().split())
result_list = [
    exact_king - king,
    exact_queen - queen,
    exact_look - look,
    exact_bishop - bishop,
    exact_knight - knight,
    exact_pone - pone
]

print(' '.join(map(str, result_list)))

