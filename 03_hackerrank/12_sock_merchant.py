# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks_distribution = {}
    result = 0
    for sock in ar:
        try:
            socks_distribution[sock] += 1
        except:
            socks_distribution[sock] = 1
    for count in list(socks_distribution.values()):
        result += (count//2)
    return result
    
if __name__ == '__main__':

    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)

