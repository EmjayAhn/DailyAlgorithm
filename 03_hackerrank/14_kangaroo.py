# https://www.hackerrank.com/challenges/kangaroo/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if x1 > x2:
        if (v2 - v1 > 0):
            if ((x1-x2) % (v2-v1) == 0):
                return 'YES'
            else:
                return 'NO'
        else:
            return 'NO'
    elif x1 < x2:
        if (v1 - v2 > 0):
            if ((x2 - x1) % (v1-v2) == 0):
                return 'YES'
            else:
                return 'NO'
        else:
            return 'NO'
    else:
        if v1 == v2:
            return 'YES'
        else:
            return 'NO'

    # jump_count = 0
    # while True:
    #     kan1_location = x1 + jump_count * v1
    #     kan2_location = x2 + jump_count * v2
    #     if kan1_location == kan2_location:
    #         return 'YES'
    #     jump_count += 1
                    
if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)