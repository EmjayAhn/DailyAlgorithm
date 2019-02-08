# baekjoon/1000
# https://www.acmicpc.net/problem/1000
def solution(A, B):
    return A + B


# testcode
def test(func):
    cases = [
        (1, 2)
    ]
    results = [3]
    for index, case in enumerate(cases):
        assert func(*case) == results[index]
    print("SUCCESS")

test(solution)
