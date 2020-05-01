#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag = {}
    _note = {}
    for w in magazine:
        if w in mag:
            mag[w] = mag[w]+1
        else:
            mag[w]=1

    for n in note:
        if n in _note:
            _note[n]+=1
        else:
            _note[n]=1

    for word in _note:
        if word in mag and _note[word]<=mag[word]:
            continue
        else:
            return "No"

    return "Yes"


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
