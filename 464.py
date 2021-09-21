class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def win(visited, target):
            if visited in log:
                return log[visited]
            i = 0
            while i < maxChoosableInteger:
                if not (visited & (1 << i)):
                    if i + 1 >= target:
                        log[visited] = True
                        return True
                    res = win(visited | (1 << i), target - i - 1)
                    if not res:
                        log[visited] = True
                        return True
                i += 1
            log[visited] = False
            return False

        su = maxChoosableInteger * (maxChoosableInteger + 1) / 2
        if desiredTotal <= maxChoosableInteger:
            return True
        elif su < desiredTotal:
            return False
        elif su == desiredTotal:
            return maxChoosableInteger % 2 != 0

        log = dict()
        return win(0, desiredTotal)


print(Solution().canIWin(3, 4))
