# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    
    wait_list = []
    for each in s:
        if each == '(':
            wait_list.append(each)
        elif each == ')':
            try:
                wait_list.pop()
            except:
                return False
    if len(wait_list) > 0:
        answer = False
    return answer