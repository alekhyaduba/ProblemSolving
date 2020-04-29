#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    num_a=0
    for char in s:
        if char=="a":
            num_a+=1

    num_a=int(n/len(s))*num_a
    remainder=n%len(s)

    for i in range(0,remainder):
        if s[i]=="a":
            num_a+=1
    return num_a



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
