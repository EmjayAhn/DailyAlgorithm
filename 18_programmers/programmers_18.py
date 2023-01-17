# https://school.programmers.co.kr/learn/courses/30/lessons/120843
# programmers, 코딩테스트 입문

def solution(numbers, k):
    return numbers[ 2 * (k - 1) % len(numbers)]

if __name__=="__main__":
    test_set = [[[1, 2, 3, 4, ], 2],
                [[1, 2, 3, 4, 5, 6, ], 5],
                [[1, 2, 3], 3]]
    for test in test_set:
        numbers, k = test
        print(solution(numbers, k))