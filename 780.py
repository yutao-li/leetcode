class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx == tx and sy == ty:
            return True
        queue = [(tx, ty)]
        a = sx % sy
        b = sy % sx
        while queue:
            q = []
            for tx, ty in queue:
                c0, c1 = tx % sy, ty % sy
                if a == 0:
                    if c0 or c1:
                        continue
                c0, c1 = tx % sx, ty % sx
                if b == 0:
                    if c0 or c1:
                        continue
                tx1 = tx - ty
                if tx1 >= 1:
                    if tx1 == sx and ty == sy:
                        return True
                    else:
                        q.append((tx1, ty))
                ty1 = ty - tx
                if ty1 >= 1:
                    if ty1 == sy and tx == sx:
                        return True
                    else:
                        q.append((tx, ty1))
            queue = q
        return False


print(Solution().reachingPoints(1, 1, 1000000000, 1))
