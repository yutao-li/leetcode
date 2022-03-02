from heapq import heappop, heappush
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sell_pq = []
        buy_pq = []
        for p, a, t in orders:
            if t == 0:
                while a and sell_pq and sell_pq[0][0] <= p:
                    if sell_pq[0][1] > a:
                        sell_pq[0][1] -= a
                        a = 0
                    else:
                        a -= sell_pq[0][1]
                        heappop(sell_pq)
                if a:
                    heappush(buy_pq, [-p, a])
            else:
                while a and buy_pq and -buy_pq[0][0] >= p:
                    if buy_pq[0][1] > a:
                        buy_pq[0][1] -= a
                        a = 0
                    else:
                        a -= buy_pq[0][1]
                        heappop(buy_pq)
                if a:
                    heappush(sell_pq, [p, a])
        return (sum(i for _, i in sell_pq) + sum(i for _, i in buy_pq)) % (10 ** 9 + 7)


print(Solution().getNumberOfBacklogOrders(orders=[[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]))
