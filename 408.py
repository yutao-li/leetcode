class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        n1 = len(word)
        n2 = len(abbr)
        while i < n1 and j < n2:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit() and abbr[j] != '0':
                k = j + 1
                while k < n2 and abbr[k].isdigit():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                return False
        return i == n1 and j == n2
