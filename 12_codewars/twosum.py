# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python

def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            answer = numbers[i] + numbers[j]
            if answer == target:
                return (i, j)
        
if __name__ == '__main__':
    print(two_sum([1, 2, 3], 4))


