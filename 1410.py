from typing import List


class Solution:
    def entityParser(self, text: str) -> str:
        return text.replace('&quot;', '"').replace('&apos;', "'").replace('&amp;', '&').replace('&gt;', '>').replace(
            '&lt;', '<').replace('&frasl;', '/')


print(Solution().entityParser("&amp; is an HTML entity but &ambassador; is not."))
