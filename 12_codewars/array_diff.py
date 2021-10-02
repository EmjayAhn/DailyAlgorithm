# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def array_diff(a, b):
    b_index = 0
    while b_index < len(b):
        if b[b_index] in a:
            a.pop(a.index(b[b_index]))
        elif b[b_index] not in a:
            b_index += 1
        
    return a

if __name__ == '__main__':
    print(array_diff([1, 2], [1]))
    print(array_diff([1, 2, 2, 2, 3], [2]))
