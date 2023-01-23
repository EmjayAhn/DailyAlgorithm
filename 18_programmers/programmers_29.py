# https://school.programmers.co.kr/learn/courses/30/lessons/120854
# programmers, 코딩테스트 입문

def solution(strlist):
    answer = []
    for each in strlist:
        answer.append(len(each))
    return answer

if __name__ == '__main__':
    test_set = [
        ["We", "are", "the", "world!"],
        ["I", "Love", "Programmers."]
    ]
    for test in test_set:
        print(solution(test))
