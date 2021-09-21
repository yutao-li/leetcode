class Solution:
    def nextClosestTime(self, time: str) -> str:
        di = set(map(int, time[:2] + time[3:]))
        gap = float('inf')
        res = []
        current = int(time[:2]) * 60 + int(time[3:])
        for i in di:
            if i <= 2:
                for j in di:
                    if i <= 1 or j <= 4:
                        for k in di:
                            if k <= 5:
                                for l in di:
                                    ts = (i * 10 + j) * 60 + k * 10 + l
                                    g = ts - current
                                    if g <= 0:
                                        g += 24 * 60
                                    if g < gap:
                                        gap = g
                                        res = [i, j, k, l]
        return str(res[0]) + str(res[1]) + ':' + str(res[2]) + str(res[3])


print(Solution().nextClosestTime("00:00"))
