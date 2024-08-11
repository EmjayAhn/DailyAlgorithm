# import sys
# from itertools import permutations

# def baseball(number, target):
#     strike = 0
#     ball = 0
#     for index, each_number in enumerate(number):
#         if each_number in target:
#             if target.index(each_number) == index:
#                 strike += 1
#             else:
#                 ball += 1
#     return strike, ball
        

# T = int(sys.stdin.readline().rstrip())
# input_list = []
# for _ in range(T):
#     input = sys.stdin.readline().split()
#     input_list.append(input)

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# candidate = list(permutations(number_list, 3))

# count = 0
# for each_number in candidate:
#     ok = True
#     for input_number in input_list:
#        if not baseball(input_number[0], each_number) == (input_number[1], input_number[2]):
#            ok = False
#     if ok:
#         count += 1
# print(count)
            

from itertools import permutations        

N = int(input())
infos = [input().split() for _ in range(N)]

ans = 0

for cur in permutations(range(1, 10), 3):
    ok = True
    
    for num, strike, ball in infos:
        real_strike = real_ball = 0
        
        for i in range(3):
            if str(cur[i]) == num[i]:
                real_strike += 1
            elif str(cur[i]) in num:
                real_ball += 1
        
        if real_strike != int(strike) or real_ball != int(ball):
            ok = False
            break
    
    if ok:
        ans += 1
        
print(ans)