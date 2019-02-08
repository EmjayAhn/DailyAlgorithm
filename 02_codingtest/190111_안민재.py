# 1번문제
from operator import add

def make_list_by_query(n, query):
    return_list = [0 for _ in range(n)]
    i = query[0]
    for _ in range(query[1] - query[0] + 1):
        return_list[i-1] = query[2]
        i = i + 1
    return return_list


def solution(n, queries):
    init = [0 for _ in range(n)]
    for query in queries:
        init = list(map(add, init, make_list_by_query(n, query)))

    init.sort()
    return init[-1]
