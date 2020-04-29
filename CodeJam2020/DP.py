#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    d = 0
    u = 0
    count = 0
    pos = 0
    for i in range(n):
        if s[i] == "D":
            d += 1
            pos -= 1
        else:
            u += 1
            pos += 1
        if u == d and pos == 0:
            if s[i] == "U":
                count += 1
                d = 0
                u = 0
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
