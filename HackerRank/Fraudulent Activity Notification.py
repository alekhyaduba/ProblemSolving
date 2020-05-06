#!/bin/python3
import statistics
import math
import os
import random
import re
import sys
from collections import Counter


def median_dict(dict_d, d):
    x = 0
    ans = []
    for key, val in sorted(dict_d.items()):
        if d % 2 != 0:
            d = int(d / 2) + 1
            if x + val < d:
                x += val
            else:
                return key
        else:
            # what to do for even
            d = int(d / 2)
            return key
            pass
    return sum(ans) / len(ans)


def temp(expenditure, d):
    dict_counts = Counter
    min_window = 201
    max_window = -1

    ans = 0
    for i, val in enumerate(expenditure):
        if i >= d:
            dict_counts[val] += 1

            dict_counts[expenditure[i - d]] -= 1
            if dict_counts[expenditure[i - d]] == 0:
                del dict_counts[expenditure[i - d]]

            median_val = median_dict(dict_counts, d)
            if 2 * median_val <= val:
                ans += 1
        else:
            dict_counts[val] += 1
    return ans


def calulateMedian(dict_t, d):
    median = 0
    sorted(dict_t.items(),key=lambda i:i[0])
    pointer = int(d / 2)
    if d % 2 != 0:
        sum = 0
        for key, value in dict_t.items():
            sum += value
            if sum >pointer:
                median = key
                break
    else:
        pointer1 = pointer + 1
        sum = 0
        a = 0
        b = 0
        for key1, value1 in dict_t.items():
            sum += value1
            if sum >pointer and a==0:
                a=key1
            if sum>pointer1:
                b=key1
                break
        median=(a+b)/2

    return median



# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count = 0

    for i in range(d, len(expenditure)):

        temp = expenditure[i - d:i]
        trail = Counter(temp)
        if expenditure[i] >= 2 * calulateMedian(trail,d):
            count += 1

    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)
    print(result)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
