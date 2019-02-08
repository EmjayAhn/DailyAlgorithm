# https://www.acmicpc.net/problem/10799
# 백준 문제 10799

while True:
    try:
        inputs = input()
        number_of_pieces = 0
        pipe_stack = list()
        for index, input in enumerate(inputs):
            if input == '(':
                pipe_stack.append('(')
            elif input == ')':
                pipe_stack.pop()
                if inputs[index-1] == '(':
                    number_of_pieces += len(pipe_stack)
                if inputs[index-1] == ')':
                    number_of_pieces += 1
        print(number_of_pieces)
    except:
        break
