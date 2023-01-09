# https://school.programmers.co.kr/learn/courses/30/lessons/120819
# programmers, 코딩테스트 입문

def solution(money):
    
    answer = [money // 5500, money % 5500]
    return answer

if __name__=='__main__':
    money = int(input())
    print(solution(money))
