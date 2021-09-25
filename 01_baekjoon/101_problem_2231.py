import sys
input_number = int(sys.stdin.readline())

tables = {}

for M in range(1, 1000000):
    string_Ms = str(M)
    N = M
    for  string_M in string_Ms:
        N += int(string_M)
    
    if N not in tables:
        tables[N] = [M]
    else:
        tables[N].append(M)

if input_number not in tables:
    print(0)
else:
    print(min(tables[input_number]))