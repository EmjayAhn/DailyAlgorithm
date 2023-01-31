# https://school.programmers.co.kr/learn/courses/30/lessons/120893
# programmmers, 코딩테스트 입문

import string

def solution(my_string):
    answer = ''
    for s in my_string:
        if s in string.ascii_lowercase:
            answer += s.upper()
        else:
            answer += s.lower()
    return answer


if __name__ == '__main__':
    test_set = ['cccCCC', 'abCdEfghIJ']

    for test in test_set:
        print(solution(test))