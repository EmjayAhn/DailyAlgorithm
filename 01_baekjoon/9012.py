N = int(input())


def VPS(input_string):
	vps_stack = []
	for each_string in input_string:
		if each_string == '(':
			vps_stack.append(each_string)
		elif each_string == ')':
			if len(vps_stack) == 0:
				return "NO"
			else:
				vps_stack.pop()

	if len(vps_stack) == 0:
		return "YES"

	else:
		return "NO"

for _ in range(N):
	input_string = input()
	print(VPS(input_string))