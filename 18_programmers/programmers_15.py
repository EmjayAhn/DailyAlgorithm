# https://school.programmers.co.kr/learn/courses/30/lessons/120840
# programmers, 코딩테스트 입문

def solution(balls, share):
    
    def factorial(n):
        if n == 1 or n== 0:
            return 1
        return n*factorial(n-1)

    answer = factorial(balls) / (factorial(balls-share) * factorial(share))

    return answer

def solution2(balls, share):
    import math
    answer = math.comb(balls, share)
    return answer

if __name__ == "__main__":
    test_set = [[3, 2], [5, 3]]
    for test in test_set:
        balls, share = test
        print(solution(balls, share))
        print(solution2(balls, share))