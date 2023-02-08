# https://school.programmers.co.kr/learn/courses/30/lessons/120894
# programmers, 코딩테스트 입문

def solution(numbers):
    number_dict = {"zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",}
    for item in number_dict:
        numbers = numbers.replace(item, number_dict[item])
    return int(numbers)

if __name__=='__main__':
    test_set = ["onetwothreefourfivesixseveneightnine", "onefourzerosixseven"]
    for test in test_set:
        print(solution(test))