# https://school.programmers.co.kr/learn/courses/30/lessons/120853
# programmers, 코딩테스트 입문

def solution(s):
    answer = 0

    s = s.split(' ')
    for index, each in enumerate(s):
        if each != "Z":
            answer += int(each)
        else:
            answer -= int(s[index-1])
        
    return answer

if __name__ == '__main__':
    test_set = ["1 2 Z 3", "10 20 30 40", "10 Z 20 Z 1", "10 Z 20 Z", "-1 -2 -3 Z"]
    for test in test_set:
        print(solution(test))
