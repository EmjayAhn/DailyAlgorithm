# https://school.programmers.co.kr/learn/courses/30/lessons/120845
# programmers, 코딩테스트 입문

def solution(box, n):
    answer = 0
    x, y, z = box
    count_x = x // n
    count_y = y // n
    count_z = z // n

    answer = count_x * count_y * count_z
    return answer


if __name__ == '__main__':
    test_set = [[[1, 1, 1], 1],
                [[10, 8, 6], 3]]

    for test in test_set:
        box, n = test
        print(solution(box, n))