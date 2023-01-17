# https://school.programmers.co.kr/learn/courses/30/lessons/120848
# programmers, 코딩테스트 입문

def solution(n):

    def factorial(num):
        factorial_result = 1
        while num >= 1:
            factorial_result *= num
            num -= 1
        return factorial_result
    
    answer = []
    i = 0
    while True:
        if factorial(i) > n:
            return max(answer)
        if factorial(i) <= n:
            answer.append(i)
            i += 1

if __name__ == '__main__':
    test_set = [3628800, 7]
    for test in test_set:
        print(solution(test))