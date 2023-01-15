# https://school.programmers.co.kr/learn/courses/30/lessons/120831
# programmers, 코딩테스트 입문

def solution(n):
	answer = 0

	for number in range(1, n+1):
		if number % 2 == 0:
			answer += number
	return answer


if __name__ == '__main__':
	test_set = [10, 4]
	for test in test_set:
		print(solution(test))
