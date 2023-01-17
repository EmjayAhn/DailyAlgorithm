# https://school.programmers.co.kr/learn/courses/30/lessons/120846
# programmers, 코딩테스트

def solution(n):
    def count_divisor(num):
        result = []
        for i in range(1, num+1):
            if num % i == 0:
                result.append(i)
        return len(result)
    
    answer = 0
    for num in range(1, n+1):
        if count_divisor(num) >=3 :
            answer += 1

    return answer

if __name__ == '__main__':
    test_set = [10, 15]
    for test in test_set:
        print(solution(test))