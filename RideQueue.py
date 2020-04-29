#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(Q):
    moves = 0

    Q = [P - 1 for P in Q]

    for i, P in enumerate(Q):
        if P - i > 2:
            print("Too chaotic")
            return

        for j in range(max(P - 1, 0), i):
            if Q[j] > P:
                moves += 1

    return str(moves)


def minBribes(q):
    swap=0
    for index,value in enumerate(q):
        if value-index-1>2:
            return "Too chaotic"
        else:
            j=max(0,value-2)
            while j<index:
                if q[j]>value:
                    swap+=1
                j+=1
    return swap



    # for i in range(1,len(q)+1):
    #     if q[i-1] - i > 2:
    #         return("Too chaotic")
    #     j=max(0,i-2)
    #     while j< q.index(i):
    #         if q[j]>i:
    #             swap+=1
    #         j+=1
    # return swap


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minBribes(q))

        # print(min_bribes(q))
