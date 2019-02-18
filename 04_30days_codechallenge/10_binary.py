# https://www.hackerrank.com/challenges/30-binary-numbers/problem

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

max_consecutive = 0
binary_n = bin(n)[2:]
split_binary = binary_n.split('0')
for item in split_binary:
    if max_consecutive < len(item):
        max_consecutive = len(item)
print(max_consecutive)