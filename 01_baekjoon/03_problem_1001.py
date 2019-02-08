# https://www.acmicpc.net/problem/1001

# input : 3 2
# output : 1

def solution(input):
    a, b = map(int, input.split())
    return a - b


def test(func):
    inputs = [
        ('3 2')
    ]
    outputs = [
        1
    ]
    for index, input in enumerate(inputs):
        assert func(input) == outputs[index]
    print("SUCCESS")

test(solution)
