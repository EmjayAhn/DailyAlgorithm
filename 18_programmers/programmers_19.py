# https://school.programmers.co.kr/learn/courses/30/lessons/120844
# programmers, 코딩테스트 입문

def solution(numbers, direction):
    if direction == "right":
        popped_number = numbers.pop()
        numbers.insert(0, popped_number)
    else:
        popped_number = numbers.pop(0)
        numbers.append(popped_number)
    return numbers

if __name__=="__main__":
    test_set = [[[1, 2, 3], "right"],
                [[4, 455, 6, 4, -1, 45, 6], "left"]]
    for test in test_set:
        numbers, direction = test
        print(solution(numbers, direction))
