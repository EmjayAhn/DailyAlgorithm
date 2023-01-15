# https://school.programmers.co.kr/learn/courses/30/lessons/120833
# programmers, 코딩테스트 입문

def solution(numbers, num1, num2):
	answer = numbers[num1:num2+1]
	return answer



if __name__=='__main__':
	test_set = [[[1, 2, 3, 4, 5], 1, 3],
				[[1, 3, 5], 1, 2]
	]

	for numbers, num1, num2 in test_set:
		print(solution(numbers, num1, num2))
