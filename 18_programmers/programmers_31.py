# https://school.programmers.co.kr/learn/courses/30/lessons/120889
# programmers, 코딩테스트 입문

def solution(sides):
    answer = 0
    longest = max(sides)
    sides.remove(longest)
    other_a, other_b = sides
    if longest < other_a + other_b:
        answer = 1
    else:
        answer = 2
    return answer


if __name__ == "__main__":
    test_set = [
        [1, 2, 3],
        [3, 6, 2],
        [199, 72, 222]
    ]
    for test in test_set:
        print(solution(test))
