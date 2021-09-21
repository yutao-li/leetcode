class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        pos = dict(zip('croak', range(5)))
        frogs = [0] * 5
        for ch in croakOfFrogs:
            frogs[pos[ch]] += 1
            if ch == 'c':
                if frogs[-1] != 0:
                    frogs[-1] -= 1
            else:
                if frogs[pos[ch] - 1] == 0:
                    return -1
                frogs[pos[ch] - 1] -= 1
        if not sum(frogs[:4]) == 0:
            return -1
        else:
            return frogs[-1]
