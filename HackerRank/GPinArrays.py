#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countTriplets function below.
def countTriplets(arr, r):
    numbers = {}
    temp = []
    count = 0
    for i in range(0,len(arr)):
        if arr[i] in numbers:
            numbers[arr[i]].extend([i])
        else:
            numbers[arr[i]]=[i]


    for key, value in numbers.items():
        a, b, c = key, key * r, key * r * r
        if b in numbers and c in numbers:
            if (a, b, c) not in temp:
                for l in numbers[a]:
                    for m in numbers[b]:
                        for n in numbers[c]:
                            if n>m>l:
                                count+=1
                temp.append((a, b, c))
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
