class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = dict()
        for ch in s:
            if ch not in char_map:
                char_map[ch] = len(char_map)
        s = [char_map[ch] for ch in s]
        char_map = dict()
        for ch in t:
            if ch not in char_map:
                char_map[ch] = len(char_map)
        t = [char_map[ch] for ch in t]
        return s == t
