# https://school.programmers.co.kr/learn/courses/30/lessons/120839
# programmers, 코딩테스트 입문

def solution(rsp):
    winning_rules = {
        "2": "0",
        "0": "5",
        "5": "2"
    }
    answer = "".join([winning_rules[item] for item in rsp])
    return answer

if __name__== "__main__":
    test_set = ["2", "205"]
    
    for test in test_set:
        print(solution(test))