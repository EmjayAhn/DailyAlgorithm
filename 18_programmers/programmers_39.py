# https://school.programmers.co.kr/learn/courses/30/lessons/120897
# programmers, 코딩테스트 입문

def solution(n):
    answer = [i + 1 for i in range(n + 1) if n % (i + 1) == 0]
    return answer

if __name__ == '__main__':
    test_set = [24, 29]
    for test in test_set:
        print(solution(test))