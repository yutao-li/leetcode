class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        states = set()
        states.add(0)
        i = 0
        while i < len(p) and p[i] == '*':
            states.add(i + 1)
            i += 1
        for i in s:
            newStates = set()
            for st in states:
                if st == len(p):
                    continue
                if p[st] == i or p[st] == '?':
                    newStates.add(st + 1)
                elif p[st] == '*':
                    newStates.add(st)

            expand = set()
            for i in newStates:
                if i in expand:
                    continue
                expand.add(i)
                while i < len(p) and p[i] == '*':
                    expand.add(i + 1)
                    i += 1

            states = expand

        if len(p) in states:
            return True
        else:
            return False


s = "acdcb"
p = "a*c?b"
print(Solution().isMatch(s, p))
