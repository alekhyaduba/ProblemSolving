#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    values = {(1, n): 0}
    max=0
    for x in queries:
        for v, c in values.items():
            a = v[0]
            b = v[1]
            if x[0] in range(a, b + 1) and x[1] > b:
                del values[(a, b)]
                if x[0]==a:
                    values[(a,a)]=c
                else:
                    values[(a, x[0] - 1)] = c
                values[(x[0], b)] = c + x[2]
                if b==x[1]:
                    values[(b,b)]=x[2]
                else:
                    values[(b + 1, x[1])] = x[2]
                if c+x[2]>max:
                    max=c+x[2]


            if x[1] in range(a, b + 1) and x[0] < a:
                del values[(a, b)]
                if x[0]==a:
                    values[a,a]=x[2]
                else:
                    values[(x[0], a - 1)] = x[2]
                values[(a, x[1])] = c + x[2]
                if x[1]==b:
                    values[(b,b)]=c
                else:
                    values[(x[1] + 1, b)] = c
                if c+x[2]>max:
                    max=c+x[2]

            if x[0] in range(a, b + 1) and x[1] in range(a, b + 1):
                del values[(a, b)]
                if x[0]!=a:
                    values[(a, x[0] - 1)] = c
                values[(x[0],x[1])]=c+x[2]
                if x[1]!=b:
                    values[x[1]+1,b]=c
                if c+x[2]>max:
                    max=c+x[2]
            break

    return max


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)

    """
    5 3
    
    """

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
