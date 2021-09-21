from typing import List
from collections import defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table = set()
        food = set()
        for _, t, f in orders:
            table.add(int(t))
            food.add(f)
        table = sorted(table)
        foodl = sorted(food)
        food = dict(zip(foodl, range(len(food))))
        disp = defaultdict(lambda: [0] * len(food))
        for _, t, f in orders:
            disp[int(t)][food[f]] += 1
        return [['Table'] + foodl] + [[str(t)] + [str(i) for i in disp[t]] for t in table]


print(Solution().displayTable([["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]))
