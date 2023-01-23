# https://school.programmers.co.kr/learn/courses/30/lessons/120888
# programmers, 코딩테스트 입문

def solution(my_string):
    answer = ''
    for s in my_string:
        if s not in answer:
            answer += s
    return answer


if __name__ == "__main__":
    test_set = ["people", "We are the world"]
    for test in test_set:
        print(solution(test))
