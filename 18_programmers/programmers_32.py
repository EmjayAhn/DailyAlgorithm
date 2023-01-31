# https://school.programmers.co.kr/learn/courses/30/lessons/120890
# programmers, 코딩테스트 입문

def solution(array, n):
    answer = 0
    array = sorted(array)
    difference = list(map(lambda x: abs(x - n), array))
    min_difference = min(difference)
    min_index = difference.index(min_difference)
    answer = array[min_index]

    return answer

# solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

if __name__=='__main__':
    test_set = [
        [[3, 10, 28], 20],
        [[10, 11, 12], 13]
    ]
    for test in test_set:
        array, n = test
        print(solution(array, n))