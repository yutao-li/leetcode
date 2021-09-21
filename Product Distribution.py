# !/bin/python3

import math
import os
import random
import re
import sys
import math


#
# Complete the 'maxScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER m
#

def maxScore(a, m):
    # Write your code here
    modu = 10 ** 9 + 7
    a.sort()
    seg = []
    q, r = divmod(len(a), m)
    for i in range(q):
        seg.append(sum(a[i * m:(i + 1) * m]))
    if r:
        for p in a[-r:]:
            seg[-1] += p
    return sum(i * j for i, j in enumerate(seg, start=1)) % modu


res = maxScore([4,1,9,7], 4)
