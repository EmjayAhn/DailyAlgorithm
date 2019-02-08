# 딕셔너리를 csv 포맷으로, csv 포맷을 딕셔너리를 담고 있는 리스트로 변환하는 함수
# 내장함수 all, any를 구현
# 딕셔너리를 value 기준으로 정렬
# 숫자(10진법)를 받아서 2진법, 8진법, 16진법으로 변환하는 각각의 함수

#2진법으로 바꾸기
def to_binary(number):
    result = ""
    while number >= 1 :
        remain = number % 2
        result += str(remain)
        number = number // 2

    return result[::-1]

#8진법으로 바꾸기
def to_octal(number):
    result = ""
    while number >= 1:
        remain = number % 8
        result += str(remain)
        number = number // 8
    return result[::-1]


#16진법으로 바꾸기
def to_hexa(number):
    result = ""

    remain_map = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    while number >= 1:
        remain = number % 16
        if remain >= 10:
            remain = remain_map[remain]
        result += str(remain)
        number = number // 16

    return result[::-1]

#내장함수 all, any 를 구현
# 내장함수 all : 1. 빈리스트가 들어올때는 True Return
# list 내의 모든 element 가 True 일때, return True, 하나라도 False 이면 return False

#내장함수 all
def my_all(inputs):
    result = True
    for input in inputs:
        result = result & input
    return result

#내장함수 any
def my_any(inputs):
    result = False
    for input in inputs:
        result = result | input
    return result


#dictionary 를 value 기준으로 sorting
def sort_dict(dictionary):
    return dict(sorted(list(dictionary.items()), key=lambda x: x[1]))


#딕셔너리를 담고있는 리스트를 csv포맷으로, csv포맷을 딕셔너리를 담고 있는 리스트로 변환하는 함수
def to_csv(dict_list):
    data = ""
    #Column name 생성
    for index, name in enumerate(list(dict_list[0].keys())):
        if index < (len(dict_list[0]) - 1):
            data += str(name) + ", "
        else:
            data += str(name) + "\n"

    #Data 쓰기
    for element in dict_list:
        for index, item in enumerate(list(element.values())):
            if index < (len(element) - 1):
                data += str(item) + ", "
            else:
                data += str(item) + "\n"

    #csv format 으로 file write
    f = open("./to_csv.csv", 'w')
    f.write(data)
    f.close()


def to_dict(csv_file):
    results = []
    path="./" + str(csv_file)
    f = open(path, 'r')
    data = f.read()
    f.close()

    splits = data.split('\n')
    keys = splits[0].split(',')
    for i in range(1, len(splits)-1):
        items = splits[i].split(',')
        results.append(dict(zip(keys, items)))
    return results
