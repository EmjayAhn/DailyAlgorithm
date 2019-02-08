# https://www.acmicpc.net/problem/10869

while True:
    try:
        input_1, input_2 = map(int, input().split())
        print(input_1 + input_2)
        print(input_1 - input_2)
        print(input_1 * input_2)
        print(input_1 // input_2)
        print(input_1 % input_2)
    except:
        break
