# https://school.programmers.co.kr/learn/courses/30/lessons/120891
# programmers, 코딩테스트 입문

def solution(order):
    answer = 0
    order = str(order)
    for s in order:
        if s in ['3', '6', '9']:
            answer += 1
    return answer



if __name__=='__main__':
    test_set = [3, 29423]
    for test in test_set:
        print(solution(test))