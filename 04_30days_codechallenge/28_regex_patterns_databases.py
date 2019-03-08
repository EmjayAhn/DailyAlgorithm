# https://www.hackerrank.com/challenges/30-regex-patterns/problem

import re

mail_regex = re.compile("^[a-z\.]+@gmail.com$")
account_dict = {}
N = int(input().strip())
for _ in range(N):
	firstName, email = input().strip().split(' ')
	if mail_regex.match(email):
		account_dict[email] = firstName

sorted_names = sorted(account_dict.values())
print(*sorted_names, sep="\n")