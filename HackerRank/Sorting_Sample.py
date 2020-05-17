#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    x=s.split(" ")
    res=""
    for i in range(0,len(x)):
        firstalph=x[i][0:1]
        rest=x[i][1:]
        res+=firstalph.capitalize()+rest+" "
    return res






if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

    # fptr.write(result + '\n')chris alan
    #
    # fptr.close()
