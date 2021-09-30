# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python
import re
def count_smileys(arr):
    count = 0
    pattern = re.compile('(:|;)(-|~)?(\)|D)')
    for strings in arr:
        match = pattern.match(strings)
        if match:
            count += 1

    return count

import sys
input_string = sys.stdin.readline()
input_array = [input_string]
print(count_smileys(input_array))