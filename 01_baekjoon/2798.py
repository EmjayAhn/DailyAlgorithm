from itertools import combinations

N, M = map(int, input().split())
card_list = list(map(int, input().split()))

temp = 0
for each_comb in combinations(card_list, 3):
	each_comb = list(each_comb)
	total_sum = sum(each_comb)

	if total_sum <= M and temp < total_sum:
		temp = total_sum

print(temp)




