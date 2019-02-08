## 1번문제
def solution(list_numbers):
    count = dict()
    for index, number in enumerate(list_numbers):
        count[number] = index, list_numbers.count(number)

    count = sorted(list(count.items()), key=lambda data: data[1][1], reverse=True)


    if count[0][1][1] > (len(list_numbers)//2):
        return count[0][1][0]
    else:
        return -1


## 2번 문제
def palindrome(string):
    if not a.islower():
        string = string.lower()

    if not a.isalpha():
        #모든 특수문자를 한번에 뽑을 수 있는 무언가 생각
        string = string.replace(",", "")

    for number in range(len(string)//2):
        if string[number] != string[len(string)-number-1]:
            return False
    return True
