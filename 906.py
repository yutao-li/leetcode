from math import sqrt


class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        count = 0
        L, R = sqrt(int(L)), int(sqrt(int(R)))
        L = int(L) if L == int(L) else int(L) + 1
        if L > R:
            return 0
        if L <= 10:
            if L <= 1 <= R:
                count += 1
            if L <= 2 <= R:
                count += 1
            if L <= 3 <= R:
                count += 1
            L = 11
        if R <= 10:
            return count
        R, L = str(R), str(L)

        q, oddR = divmod(len(R), 2)
        first = R[:q + (1 if oddR else 0)]
        second = R[-1:q - 1:-1]
        if first > second:
            R = str(int(first) - 1)
            if len(R) < len(second):
                if oddR:
                    oddR = False
                else:
                    oddR = True
                    R += '9'
        else:
            R = first

        q, odd = divmod(len(L), 2)
        first = L[:q + (1 if odd else 0)]
        second = L[-1:q - 1:-1]
        if first < second:
            L = str(int(first) + 1)
        else:
            L = first
        while True:
            pali = L + L[-2 if odd else -1::-1]
            sq = str(int(pali) ** 2)
            if sq == sq[::-1]:
                count += 1
            if L == R and odd == oddR:
                break
            next_l = int(L) + 1
            if len(str(next_l)) > len(L):
                if odd:
                    L = str(next_l // 10)
                    odd = False
                else:
                    L = str(next_l)
                    odd = True
            else:
                L = str(next_l)
        return count


print(Solution().superpalindromesInRange("1", "100000000"))
