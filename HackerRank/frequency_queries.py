#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the freqQuery function below.
def freqQuery(queries):
    ans = []
    dict_num_counts = {}
    dict_counts_count = {}
    for q in queries:
        q_type = q[0]
        num = q[1]

        if q_type == 1:
            if num in dict_num_counts:
                # increment the frequency
                dict_num_counts[num] += 1

                # update the frequency dict
                val = dict_num_counts[num]
                if val in dict_counts_count:

                    # increment the count of frequency
                    # decrement the count of frequency - 1
                    dict_counts_count[val] += 1
                    dict_counts_count[val - 1] -= 1
                    if dict_counts_count[val - 1] == 0:
                        del dict_counts_count[val - 1]
                else:
                    dict_counts_count[val] = 1
                    dict_counts_count[val - 1] -= 1
                    if dict_counts_count[val - 1] == 0:
                        del dict_counts_count[val - 1]
            else:
                dict_num_counts[num] = 1
                val = 1
                if val in dict_counts_count:
                    dict_counts_count[val] += 1
                else:
                    dict_counts_count[val] = 1

        elif q_type == 2:
            if num in dict_num_counts:
                if dict_num_counts[num] == 1:
                    val = 1
                    if val in dict_counts_count:
                        dict_counts_count[val] -= 1
                        if dict_counts_count[val] == 0:
                            del dict_counts_count[val]

                    del dict_num_counts[num]
                else:
                    val = dict_num_counts[num]
                    dict_counts_count[val] -= 1

                    if dict_counts_count[val] == 0:
                        del dict_counts_count[val]

                    if val - 1 in dict_counts_count:
                        dict_counts_count[val - 1] += 1
                    else:
                        dict_counts_count[val - 1] = 1
                    dict_num_counts[num] -= 1

        elif q_type == 3:
            if num in dict_counts_count:
                ans.append(1)
            else:
                ans.append(0)

    return ans


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')
    #
    # fptr.close()

    print(ans)
