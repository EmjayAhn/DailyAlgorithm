import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    result = []
    input_sentence = sys.stdin.readline().split()
    for each_word in input_sentence:
        backward = each_word[::-1]
        result.append(backward)
    print(' '.join(result))
    