# 1번 문제

# 2번 문제
# 가장 쉬운 버젼
def solution(n):
    if n <= 2:
        return n-1
    else:
        return solution(n-1) + solution(n-2)

def solution(n):
    mem1, mem2 = 1, 0
    for _ in range(n):
        mem1, mem2 = mem2, mem1 + mem2
    return mem1
