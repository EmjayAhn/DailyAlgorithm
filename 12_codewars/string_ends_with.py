def solution(string, ending):
    compare_pattern = string[(len(string)-len(ending)):]
    if compare_pattern == ending:
        return True
    else:
        return False


if __name__ == '__main__':
    test_string = 'abc'
    test_ending = 'bc'
    test_ending1 = 'd'

    print(solution(test_string, test_ending))
    print(solution(test_string, test_ending1))

