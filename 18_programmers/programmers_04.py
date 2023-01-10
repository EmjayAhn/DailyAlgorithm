# https://school.programmers.co.kr/learn/courses/30/lessons/120826
# programmers #코딩테스트 입문

def solution(my_string, letter):
	answer = ''
	for remove_letter in letter:
		answer = my_string.replace(remove_letter, '')
	return answer

if __name__=="__main__":
	my_string = "adfgzsklopffbcdef"
	letter = "fzsk"
	print(my_string)
	print(letter)
	print(solution(my_string, letter))
