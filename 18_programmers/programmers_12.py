# https://school.programmers.co.kr/learn/courses/30/lessons/120837
# programmers, 코딩테스트 입문

def solution(hp):
    answer = 0
    ants = {
        "general": 5,
        "soldier": 3,
        "private": 1,
    }
    for item in ants:
        answer += hp // ants[item]
        hp = hp%ants[item]

    return answer

if __name__=="__main__":
    test_set = [23, 24, 999]
    for test in test_set:
        print(solution(test))