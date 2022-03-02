from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        inventory.append(0)
        value = 0
        modulo = 10 ** 9 + 7
        for i, (j1, j2) in enumerate(zip(inventory, inventory[1:])):
            max_order = (j1 - j2) * (i + 1)
            if orders > max_order:
                orders -= max_order
                value = (value + (j1 + j2 + 1) * (j1 - j2) // 2 * (i + 1)) % modulo
            else:
                row, remainder = divmod(orders, i + 1)
                value = (value + remainder * (j1 - row) + (j1 + j1 - row + 1) * row // 2 * (i + 1)) % modulo
                return value
