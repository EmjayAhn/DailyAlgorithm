# https://school.programmers.co.kr/learn/courses/30/lessons/120834
# programmers, 코딩테스트 입문

def solution(age):
	import string

	answer = ''
	alphabet = string.ascii_lowercase
	for each_string in str(age):
		answer += alphabet[int(each_string)]

	return answer

if __name__=='__main__':
	test_set = [
		23, 51, 100
	]
	for test in test_set:
		print(solution(test))
