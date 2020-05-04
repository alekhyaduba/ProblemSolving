#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    sum=0
    c=0
    while sum<k:
        for val in prices:
            sum+=val
            if sum<k:
                c+=1

    return c





if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
