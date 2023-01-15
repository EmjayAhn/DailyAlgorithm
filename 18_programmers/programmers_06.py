# https://school.programmers.co.kr/learn/courses/30/lessons/120830
# programmers 코딩테스트 입문

def solution(n, k):
	answer = 12000*n + 2000*(k - (n//10))
	return answer

if __name__ == '__main__':
	test_set = [[10, 3], [64, 6]]
	for n, k in test_set:
		print(solution(n, k))
