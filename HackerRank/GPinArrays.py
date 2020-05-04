#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys


# Complete the countTriplets function below.
def countTriplets(arr, r):
    double=Counter()
    triple=Counter()
    count=0

    for x in arr:
        if x in triple:
            count+=triple[x]
        if x in double:
            triple[x*r]+=double[x]

        double[x*r]+=1

    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)
    print(ans)

    # fptr.write(str(ans) + '\n')
    #
    # fptr.close()
    #

    """
    1 3 3 9 9 
    5 2
    1 2 1 2 4
    
    5 5
    625 5 5 25 125
    
    1-1
    3-2
    9-2
    
    
    """
