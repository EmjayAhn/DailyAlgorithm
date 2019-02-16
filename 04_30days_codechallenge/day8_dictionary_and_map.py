# https://www.hackerrank.com/domains/tutorials/30-days-of-code?filters%5Bstatus%5D%5B%5D=unsolved&badge_type=30-days-of-code

import sys

phonebook = {}

number = int(sys.stdin.readline().rstrip('\n'))

for _ in range(number):
    input_data = sys.stdin.readline().rstrip('\n').split()
    phonebook[input_data[0]] = input_data[1]

while True:
    query = sys.stdin.readline().rstrip('\n')
    if not query:
        break
    try:
        sys.stdout.write(query + '=' + str(phonebook[query]) + '\n')
    except:
        sys.stdout.write('Not found' + '\n')


