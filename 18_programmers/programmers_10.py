# https://school.programmers.co.kr/learn/courses/30/lessons/120835
# programmers, 코딩테스트 입문


def solution(emergency):
	answer = []
	
	sort_emergency = sorted(emergency, reverse=True)
	for element in emergency:
		index = sort_emergency.index(element)
		answer.append(index+1)

	return answer


if __name__=='__main__':
	test_set = [
		[3, 76, 24],
		[1, 2, 3, 4, 5, 6, 7],
		[30, 10, 23, 6, 100]
	]

	for test in test_set:
		print(solution(test))
