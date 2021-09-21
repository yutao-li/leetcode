class Solution:
    def nextClosestTime(self, time: str) -> str:
        di = sorted(set(time[:2] + time[3:]))
        res = list(time)
        for i, bound in [(4, '9'), (3, '5'), (1, '9' if time[0] < '2' else '3'), (0, '2')]:
            pos = di.index(time[i]) + 1
            if pos < len(di) and di[pos] <= bound:
                res[i] = di[pos]
                break
            else:
                res[i] = di[0]
        return ''.join(res)


print(Solution().nextClosestTime("19:34"))
