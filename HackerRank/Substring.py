#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    for s in s1:
        if s in s2:
            return "Yes"
        else:
            continue
    return "No"
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        print(twoStrings(s1, s2))


    #     fptr.write(result + '\n')
    #
    # fptr.close()
