class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(mask, i):
            if i == 1:
                return 1
            if mask not in mem_cache:
                mem_cache[mask] = sum(dfs((1 << j) | mask, i - 1) for j in match[i] if not (1 << j) & mask)
            return mem_cache[mask]

        match = [[] for _ in range(n + 1)]
        mem_cache = dict()
        for i in range(1, n + 1):
            match[i].append(i)
            j = 2 * i
            while j <= n:
                match[i].append(j)
                match[j].append(i)
                j += i
        return dfs(0, n)


print(Solution().countArrangement(2))
