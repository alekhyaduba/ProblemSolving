

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    currentPosition=0
    numSteps=0
    while currentPosition<len(c)-2:
        if c[currentPosition+2]==0:
            currentPosition+=2
            numSteps+=1
        else:
            currentPosition+=1
            numSteps+=1
    if currentPosition==len(c)-2:
        numSteps+=1
    return  numSteps



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
