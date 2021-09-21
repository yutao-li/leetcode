from bisect import bisect


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        len_num = len(num)
        if k >= len_num * (len_num - 1) / 2:
            return ''.join(sorted(num))
        pos = [[] for _ in range(10)]
        for i in range(len_num - 1, -1, -1):
            pos[int(num[i])].append(i)
        prev = []
        ans = ''
        candi = list(range(10))
        while k and len(ans) < len_num:
            for di in candi[:]:
                if pos[di]:
                    index = pos[di][-1]
                    place = bisect(prev, index)
                    if index - place <= k:
                        prev.insert(place, index)
                        k -= index - place
                        pos[di].pop()
                        ans += str(di)
                        break
                else:
                    candi.remove(di)
        if k == 0 and len(ans) < len_num:
            prev = set(prev)
            return ans + ''.join(ch for i, ch in enumerate(num) if i not in prev)
        else:
            return ans


res = Solution().minInteger('4321', 4)
