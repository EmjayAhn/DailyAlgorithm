# https://www.hackerrank.com/challenges/30-sorting/

import sys

def bubble_sort(array):
    count = 0
    for index, _ in enumerate(array[:-1]):
        for index2, _ in enumerate(array[:-(index+1)]):
            if array[index2] > array[index2 + 1]:
                count += 1
                array[index2], array[index2 + 1] = array[index2 + 1], array[index2]
    return count, array

count = 0
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

count, a = bubble_sort(a)

print("Array is sorted in {} swaps.".format(count))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))


