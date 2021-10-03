# https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python
def sum_dig_pow(a, b):
    result = []
    for number in range(a, b+1):
        total_sum = 0
        for index, string in enumerate(str(number)):
            total_sum += int(string)**(index+1)
        if total_sum == number:
            result.append(number)

    return result


if __name__=='__main__':
    print(sum_dig_pow(1, 10))
    print(sum_dig_pow(1, 100))