N = int(input())


for _ in range(N):
    output_string = ''
    iterative_number, input_string = input().split()
    for each_letter in input_string:
       output_string += each_letter * int(iterative_number)
    print(output_string)    


    