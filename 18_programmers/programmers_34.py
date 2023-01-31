# https://school.programmers.co.kr/learn/courses/30/lessons/120892
# programmers, 코딩테스트 입문

def solution(cipher, code):
    answer = cipher[code - 1::code]

    return answer

if __name__=='__main__':
    test_set = [['dfjardstddetckdaccccdegk', 4],
    ['pfqallllabwaoclk', 2]]

    for test in test_set:
        cipher, code = test
        print(solution(cipher, code))