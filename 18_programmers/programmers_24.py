# https://school.programmers.co.kr/learn/courses/30/lessons/120849
# programmers, 코딩테스트 입문

def solution(my_string):
    answer = ''
    target = ['a', 'e', 'i', 'o', 'u']
    for s in my_string:
        if s not in target:
            answer += s
    return answer


if __name__ == '__main__':
    test_set = ['bus', 'nice to meet you']
    for test in test_set:
        print(solution(test))
