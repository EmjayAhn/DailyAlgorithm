# https://school.programmers.co.kr/learn/courses/30/lessons/120852
# programmers, 코딩테스트 입문

def check_sosu(n):
    for i in range(2, n):
        if n % i != 0:
            pass
        else:
            return False
    return True

def solution(n):
    answer = []
    for num in range(2, n+1):
        if n % num == 0:
            if check_sosu(num):
                answer.append(num)
    return answer

if __name__ == '__main__':
    print(check_sosu(2))
    print(check_sosu(3))
    print(check_sosu(4))
    test_set = [12, 17, 420]
    for test in test_set:
        print(solution(test))
