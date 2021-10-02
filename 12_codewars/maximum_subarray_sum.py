def max_sequence(arr):
    max_sum = 0
    start_index = 0
    end_index = 0
    while True:
        partial_sum = sum(arr[start_index:end_index])
        if partial_sum > max_sum:
            max_sum = partial_sum

        end_index += 1
        if end_index > len(arr):
            start_index += 1
            end_index = start_index
        if start_index > len(arr):
            break

    return max_sum




if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sequence(arr))
