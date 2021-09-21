from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 1
        count = 1
        while i < len(chars):
            while i < len(chars) and chars[i] == chars[i - 1]:
                chars.pop(i)
                count += 1
            if count > 1:
                l = list(str(count))
                chars[i:i] = l
                i += len(l) + 1
                count = 1
            else:
                i += 1
        return len(chars)


res = Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
