import string
L = int(input())
input_string = input()

alphabet = string.ascii_lowercase

sum_ = 0
for i, each_letter in enumerate(input_string):
	sum_ += (alphabet .index(each_letter)+1)*(31**i)
	

print(sum_ % 1234567891)
