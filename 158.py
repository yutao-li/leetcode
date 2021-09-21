# The read4 API is already defined for you.
from typing import List


def read4(buf: List[str]) -> int:
    pass


class Solution:
    def __init__(self):
        self.trail = []

    def read(self, buf: List[str], n: int) -> int:
        tmp = [""] * 4
        j = 0
        le = len(self.trail)
        if le:
            if le <= n:
                buf[:le] = self.trail
                j += le
                n -= le
                self.trail = []
            else:
                buf[:n] = self.trail[:n]
                self.trail = self.trail[n:]
                return n
        q, r = divmod(n, 4)
        for _ in range(q):
            i = read4(tmp)
            if i != 4:
                buf[j:j + i] = tmp[:i]
                j += i
                return j
            buf[j:j + 4] = tmp
            j += 4
        if r:
            i = read4(tmp)
            k = min(r, i)
            buf[j:j + k] = tmp[:k]
            j += k
            if k < i:
                self.trail = tmp[k:i]
        return j
