#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    dict_res={}
    result=[]

    for item in queries:
        com=item[0]
        val=item[1]
        if com==1:
            if val in dict_res:
                dict_res[val]+=1
            else:
                dict_res[val]=1
        elif com==2:
            if val in dict_res:
                if dict_res[val]==1:
                    del dict_res[val]
                else:
                    dict_res[val]-=1
        elif com==3:
            set_val=set(dict_res.values())
            if val in set_val:
                result.append(1)
            else:
                result.append(0)

    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    for x in ans:
        print(x)
    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')
    #
    # fptr.close()
