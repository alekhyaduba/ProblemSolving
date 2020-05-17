#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    val=arr[-1]
    flag=True
    for i in range(n-2,-1,-1):
        if arr[i]>val:
            arr[i+1]=arr[i]
            print(*arr, sep=" ")
            flag=False
        else:
            arr[i+1]=val
            print(*arr,sep=" ")
            flag=True
            break
    if flag==False:
        arr[0]=val
        print(*arr,sep=" ")




if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
