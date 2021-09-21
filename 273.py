class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        pos = ["Thousand", "Million", "Billion"]
        digit = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        ten = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        p = -1
        res = []
        while num:
            num, n = divmod(num, 1000)
            if n and p >= 0:
                res.append(pos[p])
            p += 1
            n, r = divmod(n, 100)
            q, r1 = divmod(r, 10)
            if 11 <= r <= 19:
                res.append(ten[r - 11])
            else:
                if r1:
                    res.append(digit[r1 - 1])
                if q:
                    res.append(tens[q - 1])
            if n:
                res.append('Hundred')
                res.append(digit[n - 1])
        return ' '.join(res[::-1])


res = Solution().numberToWords(1234567891)
