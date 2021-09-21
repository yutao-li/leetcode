from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def process(li):
            if not li:
                return []
            res = [0 for _ in range(len(li))]
            res[-1] = [None] * 10
            res[-1][li[-1]] = len(li) - 1
            for i in range(len(li) - 2, -1, -1):
                res[i] = res[i + 1].copy()
                res[i][li[i]] = i
            return res

        def update(li, nums, front, k):
            while k:
                d = 9
                while li[front][d] is None or len(nums) - li[front][d] < k:
                    d -= 1
                rest = len(nums) - li[front][d]
                if rest == k:
                    return res + nums[li[front][d]:]
                elif rest > k:
                    front = li[front][d] + 1
                    k -= 1
                    res.append(d)
            return res

        le1, le2 = len(nums1), len(nums2)
        li1 = process(nums1)
        li2 = process(nums2)
        res = []
        pool = [(0,) * 2]
        while k:
            if len(pool) == 1 and (pool[0][0] == le1 or pool[0][1] == le2):
                break
            digits = []
            for front1, front2 in pool:
                if front1 < le1 and front2 < le2:
                    d1, d2 = 9, 9
                    while li1[front1][d1] is None or le1 - li1[front1][d1] + le2 - front2 < k:
                        d1 -= 1
                    while li2[front2][d2] is None or le2 - li2[front2][d2] + le1 - front1 < k:
                        d2 -= 1
                    if d1 > d2:
                        digits.append((d1, 0))
                    elif d1 < d2:
                        digits.append((d2, 1))
                    else:
                        digits.append((d1, 2))
                elif front1 < le1:
                    d1 = 9
                    while li1[front1][d1] is None or le1 - li1[front1][d1] + le2 - front2 < k:
                        d1 -= 1
                    digits.append((d1, 0))
                else:
                    d2 = 9
                    while li2[front2][d2] is None or le2 - li2[front2][d2] + le1 - front1 < k:
                        d2 -= 1
                    digits.append((d2, 1))

            max_digit = max(i[0] for i in digits)
            res.append(max_digit)
            k -= 1
            rest = [(i, o) for i, (d, o) in enumerate(digits) if d == max_digit]
            pool1 = set()
            for i, o in rest:
                front1, front2 = pool[i]
                if o == 0:
                    front1 = li1[front1][max_digit] + 1
                    pool1.add((front1, front2))
                elif o == 1:
                    front2 = li2[front2][max_digit] + 1
                    pool1.add((front1, front2))
                else:
                    front1_ = li1[front1][max_digit] + 1
                    front2_ = li2[front2][max_digit] + 1
                    pool1.add((front1_, front2))
                    pool1.add((front1, front2_))
            pool = list(pool1)
        if k:
            front1, front2 = pool[0]
            if front1 < le1:
                res = update(li1, nums1, front1, k)
            else:
                res = update(li2, nums2, front2, k)
        return res


print(Solution().maxNumber([], [1], 1))
