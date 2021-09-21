from bisect import bisect_left


class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] != 1:
            return False
        return self.dp(1, 1, {}, stones)

    def dp(self, pos, k, mem, stones):
        if pos == len(stones) - 1:
            return True
        if (pos, k + 1) not in mem:
            next_pos = bisect_left(stones[pos + 1:], stones[pos] + k + 1) + pos + 1
            if next_pos == len(stones):
                mem[pos, k + 1] = False
            elif stones[next_pos] == stones[pos] + k + 1:
                mem[pos, k + 1] = self.dp(next_pos, k + 1, mem, stones)
            else:
                mem[pos, k + 1] = False
        if mem[pos, k + 1]:
            return True

        if (pos, k) not in mem:
            next_pos = bisect_left(stones[pos + 1:], stones[pos] + k) + pos + 1
            if next_pos == len(stones):
                mem[pos, k] = False
            elif stones[next_pos] == stones[pos] + k:
                mem[pos, k] = self.dp(next_pos, k, mem, stones)
            else:
                mem[pos, k] = False
        if mem[pos, k]:
            return True

        if k > 1:
            if (pos, k - 1) not in mem:
                next_pos = bisect_left(stones[pos + 1:], stones[pos] + k - 1) + pos + 1
                if next_pos == len(stones):
                    mem[pos, k - 1] = False
                elif stones[next_pos] == stones[pos] + k - 1:
                    mem[pos, k - 1] = self.dp(next_pos, k - 1, mem, stones)
                else:
                    mem[pos, k - 1] = False
            if mem[pos, k - 1]:
                return True

        return False


stones = [0, 1, 2, 3, 4, 8, 9, 11]
print(Solution().canCross(stones))
