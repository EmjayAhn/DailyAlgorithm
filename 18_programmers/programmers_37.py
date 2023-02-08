# https://school.programmers.co.kr/learn/courses/30/lessons/120895
# programmers, 코딩테스트 입문

def solution(my_string, num1, num2):
    answer = []
    s_num1 = my_string[num1]
    s_num2 = my_string[num2]
    for index, s in enumerate(my_string):
        if index == num1:
            answer.append(s_num2)
        elif index == num2:
            answer.append(s_num1)
        else:
            answer.append(s)
    answer = ''.join(answer)
    return answer


if __name__ == '__main__':
    test_set = [["hello", 1, 2],["I love you", 3, 6]]
    for test in test_set:
        my_string, num1, num2 = test
        print(solution(my_string, num1, num2))