#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMaxCharCount' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. 2D_INTEGER_ARRAY queries
#

def getMaxCharCount(s, queries):
    # queries is a n x 2 array where queries[i][0] and queries[i][1] represents x[i] and y[i] for the ith query.
    st = [0] * len(s) + [[ch.lower(), 1] for ch in s]
    for i in range(len(s) - 1, 0, -1):
        if st[2 * i][0] == st[2 * i + 1][0]:
            st[i] = [st[2 * i][0], st[2 * i][1] + st[2 * i + 1][1]]
        else:
            st[i] = max(st[2 * i], st[2 * i + 1])
    res = []
    for i, j in queries:
        i += len(s)
        j += len(s)
        m = ['a', 0]
        while i <= j:
            if i % 2:
                if st[i][0] == m[0]:
                    m[1] += st[i][1]
                else:
                    m = max(m, st[i][:])
                i += 1
            if j % 2 == 0:
                if st[j][0] == m[0]:
                    m[1] += st[j][1]
                else:
                    m = max(m, st[j][:])
                j -= 1
            i //= 2
            j //= 2
        res.append(m[1])
    return res


def golden(s, queries):
    s = s.lower()
    return [s[i:j + 1].count(max(s[i:j + 1])) for i, j in queries]


from random import randint
from string import ascii_letters

while True:
    N = randint(1, 20)
    Q = randint(1, 20)
    S = ''.join(ascii_letters[randint(0, 51)] for _ in range(N))
    queries = []
    for _ in range(Q):
        i = randint(0, N - 1)
        j = randint(i, N - 1)
        queries.append([i, j])
    res = getMaxCharCount(S, queries)
    res1 = golden(S, queries)
    if res != res1:
        print(S)
        i = 0
        while res[i] == res1[i]:
            i += 1
        print(queries)
        print(res[i], res1[i])
        print(queries[i])
        break

res = getMaxCharCount('sVRrBgS', [[4, 4], [1, 6], [2, 5], [2, 6], [3, 6], [5, 6], [0, 6], [6, 6], [2, 2]])
res1 = golden('sVRrBgS', [[4, 4], [1, 6], [2, 5], [2, 6], [3, 6], [5, 6], [0, 6], [6, 6], [2, 2]])
