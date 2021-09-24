import sys

def prime_number(n):
    div = 2
    if n == 1:
        return False
    while(True):
        if div > n**0.5:
            break
        if n % div == 0:
            return False
        div += 1
    return True

T = int(sys.stdin.readline())
for _ in range(T):
    input_number = int(sys.stdin.readline())
    prime1_lists = []
    prime2_lists = []
    differences = []
    for n in range(2, input_number//2+1):
        if prime_number(n) and prime_number(input_number - n):
            prime1_lists.append(n)
            prime2_lists.append(input_number - n)
            differences.append(abs(n-(input_number-n)))

    if len(prime1_lists) == 1:
        print(prime1_lists[0], prime2_lists[0])
    else:
        index = differences.index(min(differences))
        print(prime1_lists[index], prime2_lists[index])

