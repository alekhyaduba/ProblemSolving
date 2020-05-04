#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swaps=0
    for i in range(0,len(a)):
        for j in range(0,len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swaps+=1
    return (swaps,a)

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    res=countSwaps(a)
    print("Array is sorted in "+str(res[0])+" swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[-1]))

