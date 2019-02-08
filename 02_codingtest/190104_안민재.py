# 첫번째 문제
def solution(A, k):
    count = 0
    while len(A) != 0:
        if (min(A) + k) in A:
            count += 1
            A.remove(min(A))
        else:
            A.remove(min(A))
    return count

# 두번째 문제
def solution(A):
    count = 0
    for index, item in enumerate(A):
        if item == 0:
            count += sum(A[index:])
        else:
            count += 0

    return count
