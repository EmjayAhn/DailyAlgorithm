# https://www.hackerrank.com/challenges/2d-array/problem

def hourglasssum(arr):
        total_sum = list()
        for i in range(0, 4):
                for j in range(0, 4):
                        total_sum.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
        return max(total_sum)
        

# test code
a = [[1, 1, 1, 0, 0, 0],\
    [0, 1, 0, 0, 0, 0],\
    [1, 1, 1, 0, 0, 0],\
    [0, 0, 2, 4, 4, 0],\
    [0, 0, 0, 2, 0, 0],\
    [0, 0, 1, 2, 4, 0]]

print(hourglasssum(a))

# print(hourglasssum(a) == 19)
