while True:

    input_list = list(map(int, input().split()))
    input_list = sorted(input_list)
    A, B, C = input_list
    if A == 0:
        break
    if C**2 == (A**2) + (B**2):
        print("right")
    else:
        print("wrong")