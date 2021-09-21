from typing import List
from heapq import *


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def transfer(fro, to):
            num, ind = heappop(fro)
            while ind <= i - k:
                num, ind = heappop(fro)
            heappush(to, (-num, ind))

        mid, r = divmod(k, 2)
        lower = [(-num, i) for i, num in enumerate(nums[:k])]
        heapify(lower)
        upper = []
        for _ in range(mid):
            num, i = heappop(lower)
            heappush(upper, (-num, i))
        res = [-lower[0][0] if r else (upper[0][0] - lower[0][0]) / 2]
        balance = r
        for i, n in enumerate(nums[k:], k):
            if upper and (nums[i - k], i - k) >= upper[0]:
                balance += 1
            else:
                balance -= 1
            heappush(upper, (n, i))
            transfer(upper, lower)
            balance += 1
            if balance > 1:
                transfer(lower, upper)
                balance -= 2
            elif balance < -1:
                transfer(upper, lower)
                balance += 2
            while lower[0][1] <= i - k:
                heappop(lower)
            while upper and upper[0][1] <= i - k:
                heappop(upper)
            res.append(-lower[0][0] if r else (upper[0][0] - lower[0][0]) / 2)
        return res


print(Solution().medianSlidingWindow([1, 2], 1))
