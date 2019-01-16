# baekjoon/2557
def solution():
    return "Hello World!"


# testcode
def test(func):
    results = [
        'Hello World!'
    ]
    for _ in results:
        assert func() == results[0]
    print("SUCCESS")


test(solution)
