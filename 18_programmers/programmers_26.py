# https://school.programmers.co.kr/learn/courses/30/lessons/120851
# programmers, 코딩테스트 입문

def solution(my_string):
    answer =sum([int(num) for num in my_string if num.isnumeric()])
    return answer

if __name__ == '__main__':
    test_set = ['aAb1B2cC34oOp', '1a2b3c4d123']
    for test in test_set:
        print(solution(test))
