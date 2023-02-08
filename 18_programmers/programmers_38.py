# https://school.programmers.co.kr/learn/courses/30/lessons/120896
# programmers, 코딩테스트 입문

def solution(s):

    answer = sorted([char for char in s if s.count(char) == 1])
    answer = ''.join(answer)

    return answer

if __name__ == '__main__':
    test_set = ["abcabcadc", "abdc", "hello"]
    for test in test_set:
        print(solution(test))