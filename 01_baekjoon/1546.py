N = int(input())
score_list = list(map(int, input().split()))


new_score_list = []
max_score = max(score_list)

for each_score in score_list:
	each_score = each_score / max_score * 100
	new_score_list.append(each_score)

print(sum(new_score_list)/N)
