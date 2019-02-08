# 1번 문제
def solution(data, queries):
    total_sum = sum(data)
    return_list = list()

    for query in queries:
        answer = total_sum - (sum(data[:query[0]-1]) + sum(data[query[1]:]))
        return_list.append(answer)

    return return_list

# 2번 문제
def solution(n):
    number_of_digit = [i+1 for i in range(n)]
    answer = 0
    for digit in number_of_digit:
        if digit%2 == 1:
            mok = digit // 2
            if mok == 0:
                result = 10
            else:
                result = 9*(10**mok)
        else:
            mok = digit // 2
            result = 9*(10**(mok-1))
        answer += result
    return answer
