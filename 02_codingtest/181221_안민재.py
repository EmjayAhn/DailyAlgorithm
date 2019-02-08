def solution(arr):
    count = 0
    temp = arr.copy()

    for cnt in range(len(arr)):
        maximum_index = temp.index(max(temp))
        if arr[maximum_index] != arr[-(cnt+1)]:
            arr[maximum_index], arr[-(cnt+1)] = arr[-(cnt+1)], arr[maximum_index]
            count += 1
        temp = arr[0:-(cnt+1)].copy()
        
    return count
