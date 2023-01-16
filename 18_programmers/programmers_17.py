# https://school.programmers.co.kr/learn/courses/30/lessons/120842
# programmers, 코딩테스트 입문

def solution(num_list, n):
    answer = []
    
    i = 0
    while i < len(num_list):
        element = num_list[i:i+n]
        answer.append(element)
        i += n
    return answer

if __name__=="__main__":
    test_set = [[[1, 2, 3, 4, 5, 6, 7, 8], 2],
                [[100, 95, 2, 4, 5, 6, 18, 33, 948], 3]]
    for test in test_set:
        num_list, n = test
        print(solution(num_list, n))