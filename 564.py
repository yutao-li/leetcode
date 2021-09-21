class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length != 1 and n[:-1] == '1' + '0' * (length - 2) and (n[-1] == '0' or n[-1] == '1'):
            return '9' * (length - 1)
        elif n == '9' * length and length != 1:
            return '1' + '0' * (length - 1) + '1'
        isPalindrome = True
        for i in range(length // 2):
            if n[i] != n[length - 1 - i]:
                isPalindrome = False
                break
        if isPalindrome:
            mid = int(n[length // 2])
            mid = mid - 1 if mid != 0 else mid + 1
            if length % 2 == 0:
                return n[:length // 2 - 1] + str(mid) * 2 + n[length // 2 + 1:]
            else:
                return n[:length // 2] + str(mid) + n[length // 2 + 1:]
        else:
            pos = length // 2 + 1 if length % 2 else length // 2
            same = n[:pos] + n[:length // 2][::-1]
            front = int(n[:pos])
            add1 = str(front + 1)
            sub1 = str(front - 1)
            if length % 2:
                incr = add1 + add1[:-1][::-1]
                decr = sub1 + sub1[:-1][::-1]
            else:
                incr = add1 + add1[::-1]
                decr = sub1 + sub1[::-1]
            num = int(n)
            candi = [(abs(int(same) - num), same), (int(incr) - num, incr), (num - int(decr), decr)]
            return min(candi)[1]


print(Solution().nearestPalindromic("1213"))
