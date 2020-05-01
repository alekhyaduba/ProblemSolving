#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count=0
    lis=[]
    dic={}

    for l in range(1,len(s)):
        for i in range(0,len(s)):
            if i+l<=len(s):
                lis.append("".join(sorted(s[i:i+l])))


    for each in lis:
        if each in dic:
            dic[each]+=1
        else:
            dic[each]=1

    for key,val in dic.items():
        count+=int((val)*(val-1)/2)

    return count



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        print(result)

    #     fptr.write(str(result) + '\n')
    #
    # fptr.close()
