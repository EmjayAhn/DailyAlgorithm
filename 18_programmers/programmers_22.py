# https://school.programmers.co.kr/learn/courses/30/lessons/120847
# programmers, 코딩테스트 입문

def solution(numbers):
    max_1 = max(numbers)

    max_index = numbers.index(max_1)
    numbers.pop(max_index)
    
    max_2 = max(numbers)
    
    answer = max_1 * max_2
    return answer

if __name__ == "__main__":
    test_set = [[1, 2, 3, 4, 5], [0, 31, 24, 10, 1, 9]]

    for test in test_set:
        print(solution(test))