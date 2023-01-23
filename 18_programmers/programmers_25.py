# https://school.programmers.co.kr/learn/courses/30/lessons/120850
# programmers, 코딩테스트 입문

def solution(my_string):
    answer = []
    for s in my_string:
        if s.isnumeric():
            answer.append(int(s))
    
    answer = sorted(answer)
    
    return answer

if __name__ == '__main__':
    test_set = ['hi12392', 'p2o4i8gj2', 'abcde0']
    for test in test_set:
        print(solution(test))

