#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap=0
    arr=[p-1 for p in arr]
    slist=[]
    for index, value in enumerate(arr):
        slist.append([value,index])
    arrList=copy.deepcopy(slist)
        # slist.copy()
    slist.sort()
    for val,ind in arrList:
        if val>ind:
            m=slist[ind][1]
            arrList[ind][0],arrList[m][0]=arrList[m][0],arrList[ind][0]
            slist[val][1]=m
            swap+=1
    return swap
"""
6
2 6 3 5 1 4
"""


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)
    # fptr.write(str(res) + '\n')
    #
    # fptr.close()
