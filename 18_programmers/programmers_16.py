# https://school.programmers.co.kr/learn/courses/30/lessons/120841
# programmers, 코딩테스트 입문

def solution(dot):
    answer = 0
    x, y = dot
    if x > 0 and y > 0:
        answer = 1
    elif x < 0 and y > 0:
        answer = 2
    elif x < 0 and y < 0:
        answer = 3
    else:
        answer = 4
    return answer

if __name__=="__main__":
    test_set = [[2, 4], [-7, 9]]
    for test in test_set:
        print(solution(test))
    