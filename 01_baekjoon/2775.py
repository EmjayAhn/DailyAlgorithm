# T = int(input())


# def how_many(k, n):
# 	if k == 0:
# 		return n
# 	result = 0
# 	for i in range(1, n+1):
# 		result += how_many(k-1, i)

# 	return result


# for _ in range(T):
# 	k = int(input())
# 	n = int(input())

# 	# 0 층 1호 : 1명
# 	# 0 층 2호 : 2명
# 	# 1 층 1호 : 1명
# 	# 1 층 2호 : 0층의 1호 부터 2호 : 1명 + 2명 = 3명
# 	# 1 층 3호 : 0층의 1호 부터 3호 : 1 + 2 +3 
# 	# 2 층 2호 : 1층의 1호부터 2호 : 1명 + 3명 = 4명
# 	result = 0
# 	result = how_many(k, n)
# 	print(result)

def how_many(k, n):
	if k == 0:
		return n

	
T = int(input())

for _ in range(T):
	k = int(input())
	n = int(input())

	memory = {}

