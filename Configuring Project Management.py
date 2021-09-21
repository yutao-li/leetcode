#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'configureProjectPresentation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY friendships
#
from collections import defaultdict


def configureProjectPresentation(n, friendships):
    # Write your code here
    fs = defaultdict(set)
    for i, j in friendships:
        fs[i].add(j)
        fs[j].add(i)
    res = set(fs[1])
    if 2 in res:
        res.remove(2)
    res -= fs[2]
    for i in fs[2]:
        if i != 1:
            res -= fs[i]
    if res:
        return sorted(res)
    else:
        return [-1]


fs = [[1, 3], [1, 4], [3, 2], [5, 6], [7, 1], [2, 8], [8, 9], [9, 1]]
res = configureProjectPresentation(9, fs)
