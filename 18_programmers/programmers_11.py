# https://school.programmers.co.kr/learn/courses/30/lessons/120836
# programmers, 코딩테스트 입문


def solution(n):
	answer = 0

	a = 0
	while a <= n:
		a += 1
		if n % a == 0:
			answer += 1
	return answer


if __name__=='__main__':
	test_set = [20, 100]
	for test in test_set:
		print(solution(test))
