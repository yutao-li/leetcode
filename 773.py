from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))
        diff = ((0, 0), (0, 0, 0), (0, -1), (0, 0), (0, 0, -1), (1, 1))
        num = sum((1 if k else 1000) * 10 ** (2 - i) * j for k, row in enumerate(board) for i, j in enumerate(row))
        df = 0
        n = num
        for i in range(6, 0, -1):
            n, r = divmod(n, 10)
            df += r != i % 6
        queue = [(df, num)]
        count = 0
        seen = {num}
        while queue:
            q1 = []
            for d, n in queue:
                if d == 0:
                    return count
                index = 5
                q, r = divmod(n, 10)
                while r:
                    index -= 1
                    q, r = divmod(q, 10)
                for i, j in zip(moves[index], diff[index]):
                    d1 = d
                    digit = n // (10 ** (5 - i)) % 10
                    n1 = n - digit * 10 ** (5 - i) + digit * 10 ** (5 - index)
                    if n1 in seen:
                        continue
                    seen.add(n1)
                    if digit - 1 == i:
                        d1 += 1
                    elif digit - 1 == index:
                        d1 -= 1
                    q1.append((d1 + j, n1))
            count += 1
            queue = sorted(q1)
        return -1


res = Solution().slidingPuzzle([[3, 2, 4], [1, 5, 0]])
