class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return len(set(A)) < len(A)
        tmp = []
        for a, b in zip(A, B):
            if a != b:
                tmp.append((a, b))
                if len(tmp) > 2:
                    return False
        return len(tmp) == 2 and tmp[0][0] == tmp[1][1] and tmp[0][1] == tmp[1][0]


print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
