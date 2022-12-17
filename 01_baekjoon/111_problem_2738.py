# https://www.acmicpc.net/problem/2738

N, M = map(int, input().split())

first_matrix = []
second_matrix = []
result_matrix = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    first_matrix.append(tmp)

for _ in range(N):
    tmp = list(map(int, input().split()))
    second_matrix.append(tmp)

for index, row in enumerate(first_matrix):
    result_row = []
    second_matrix_row = second_matrix[index]
    for each_item_index, each_item in enumerate(row):
        result_tmp = each_item + second_matrix_row[each_item_index]
        result_row.append(result_tmp)
    result_matrix.append(result_row)

for each_row in result_matrix:
    print(*each_row)