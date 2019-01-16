# testcode
def solution():
    return "Hello"

def test(func):
    results = [
        'Hello World!'
    ]
    for _ in results:
        assert func() == results[0]

    print("SUCCESS")

test(solution)
