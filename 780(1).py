class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while True:
            if tx < ty:
                sx, sy, tx, ty = sy, sx, ty, tx
            if sx == tx and sy == ty:
                return True
            if sx > tx or sy > ty:
                return False
            if tx == ty:
                return False
            elif sx < ty:
                tx %= ty
            else:
                return (tx - sx) % ty == 0 and sy == ty


print(Solution().reachingPoints(1, 1, 1000000000, 1))
