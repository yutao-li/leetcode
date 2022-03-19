from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i1 = 0
        i2 = 0
        res = []
        n1 = len(firstList)
        n2 = len(secondList)
        while i1 < n1 and i2 < n2:
            s1, e1 = firstList[i1]
            s2, e2 = secondList[i2]
            low = max(s1, s2)
            high = min(e1, e2)
            if low <= high:
                res.append([low, high])
            if e1 < e2:
                i1 += 1
            else:
                i2 += 1
        return res
