class Solution:
    def minFlips(self, target: str) -> int:
        target = target.lstrip('0')
        if not target:
            return 0
        res = 0
        for ch1, ch2 in zip(target[1:], target):
            if ch1 != ch2:
                res += 1
        return res + 1


res = Solution().minFlips(target="00000")

