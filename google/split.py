from collections import Counter


def function(S: str):
    res = 0
    left = set()
    right = Counter(S)
    for ch in S[:-1]:
        left.add(ch)
        right[ch] -= 1
        if right[ch] == 0:
            del right[ch]
            if len(right) < len(left):
                break
        if len(left) == len(right):
            res += 1
    return res

import numpy as np
arr=np.random.randint(0,26,)