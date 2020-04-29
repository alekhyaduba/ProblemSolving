#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sumList=[]
    for y in range(0,4):
        for x in range(0,4):
            sum = 0
            for j in range(y,y+3,2):
                for i in range(x,x+3):
                    sum+=arr[j][i]
            sum+=arr[y+1][x+1]
            sumList.append(sum)
    return max(sumList)





if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(arr)
    result = hourglassSum(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
