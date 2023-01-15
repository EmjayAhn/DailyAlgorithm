# https://school.programmers.co.kr/learn/courses/30/lessons/120829
# programmers, 코딩테스트 입문

def solution(angle):
	answer = 0

	if angle == 180:
		answer = 4
	elif angle >  90:
		answer = 3
	elif angle ==  90:
		answer = 2
	elif angle < 90:
		answer = 1
	
	return answer


if __name__ == '__main__':
	test_set = [70, 91, 180]
	for test in test_set:
		print(solution(test))
