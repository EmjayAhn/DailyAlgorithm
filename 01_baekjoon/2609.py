A, B = map(int, input().split())

def get_divisors(n):
	s = set()
	for i in range(1, int(sqrt(n))+1):
		if n%i == 0:
			