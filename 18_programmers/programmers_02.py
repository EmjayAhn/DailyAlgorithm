# https://school.programmers.co.kr/learn/courses/30/lessons/120820
# programmers, 코딩테스트 입문

def solution(age):
    answer = 2022 - age + 1
    return answer

if __name__ == '__main__':
    input_age = int(input())
    print(solution(input_age))