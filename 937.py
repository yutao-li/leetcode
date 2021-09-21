from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def key(x):
            pos = x.find(' ')
            return (x[pos + 1:], x[:pos])

        letter = []
        digit = []
        for log in logs:
            if log.split()[1].isalpha():
                letter.append(log)
            else:
                digit.append(log)
        return sorted(letter, key=key) + digit


print(Solution().reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
