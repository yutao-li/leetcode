from itertools import product
from typing import List


class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        def oneMove(pos: [int, int], status: int):
            count = 0
            for i in range(1 << n):
                if i & status != i:
                    continue
                status1 = status ^ i
                if status1 == 0:
                    continue
                pos1 = pos[:]
                for j, ((x0, y0), (x1, y1)) in enumerate(zip(pos, shift)):
                    if (1 << j) & status1 == 0:
                        continue
                    pos1[j] = (x0 + x1, y0 + y1)
                if any(j < 1 or j > 8 for pair in pos1 for j in pair):
                    continue
                if len(set(pos1)) < n:
                    continue
                if tuple(pos1) in seen:
                    continue
                seen.add(tuple(pos1))
                count += 1 + oneMove(pos1, status1)
            return count

        orthogonal = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        directions = {'rook': orthogonal, 'queen': orthogonal + diagonal, 'bishop': diagonal}
        n = len(pieces)
        positions = [tuple(i) for i in positions]
        seen = set()
        count = 1
        for shift in product(*(directions[i] for i in pieces)):
            count += oneMove(positions, (1 << n) - 1)
        return count


print(Solution().countCombinations(["queen", "bishop"], [[5, 7], [3, 4]]))
