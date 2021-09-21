from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [i - j for i, j in zip(gas, cost)]
        left, right = 0, -1
        cur = 0
        while len(gas) > left != right - len(gas):
            right += 1
            cur += diff[right % len(gas)]
            while left < len(gas) and cur < 0:
                cur -= diff[left]
                left += 1
        return left if left != len(gas) else -1


print(Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]))
