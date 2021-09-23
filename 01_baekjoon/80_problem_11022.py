import sys

T = sys.stdin.readline()

for i in range(int(T)):
    input_1, input_2 = sys.stdin.readline().split()
    print('Case #'+str(i+1)+': ' + input_1 + ' + ' + input_2 + ' = ' + 
           str(int(input_1)+int(input_2)))
    

