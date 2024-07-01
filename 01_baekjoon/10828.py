import sys
N = int(sys.stdin.readline())


stack = []
for _ in range(N):
	input_command = sys.stdin.readline().split()

	if input_command[0] == "push":
		stack.append(int(input_command[1]))

	elif input_command[0] == "pop":
		if len(stack) == 0:
			print(-1)
		else:
			popped = stack.pop()
			print(popped)
	
	elif input_command[0] == "size":
		print(len(stack))

	elif input_command[0] == "empty":
		if len(stack) == 0:
			print(1)
		else:
			print(0)

	else:
		if len(stack) == 0:
			print(-1)
		else:
			print(stack[-1])
