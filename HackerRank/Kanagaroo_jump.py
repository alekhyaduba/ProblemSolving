#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (((x1 < x2) and (v1 > v2)) or ((x1 > x2) and (v1 < v2))):
        n = 1
        if x1 < x2:
            b_pos = x1
            b_v = v1
            a_pos = x2
            a_v = v2
        else:
            b_pos = x2
            b_v = v2
            a_pos = x1
            a_v = v1
        while (b_pos <= a_pos):
            if b_pos == a_pos:
                return "YES"
            b_pos += (b_v)
            a_pos += (a_v)
            n += 1

    return "NO"


if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)
