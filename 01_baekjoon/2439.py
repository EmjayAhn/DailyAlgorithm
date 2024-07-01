N = int(input())

for i in range(1, N+1):
    output_string = ' '*(N-i) + '*'*(i)
    print(output_string)