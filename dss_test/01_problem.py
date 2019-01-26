# 채점하기
# 매주 금요일 알고리즘 테스트 결과를 채점하기 귀찮아졌습니다.
#
# 그래서 직접하지 않고, 수강생분들에게 공부가 된다는 사탕발림으로 서로의 시험결과를 채점하게 하려고합니다.
#
# 단, 양심적으로 진행하기 위해서 그 누구도 자신의 시험을 채점하지 않는다고 할때.
#
# 채점할 수 있는 경우의 수를 구하는 함수를 구하세요.
#
# 는
#
# n=1일때 0개 n=2일때 1개 그리고 n>=3일때
#
# (n-1) * ( (n-1)명이서 서로 채점하는 경우의 수 + (n-2)명이서 서로 채점하는 경우의 수)) 라는 특징을 따른다고 합니다.
#
# def solution(n):함수를 생성하세요.
#
# 조건
#
# 1 <= n <= 1000
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