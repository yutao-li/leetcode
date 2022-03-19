from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(i):
            while i != parent[i]:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        def union(i, j):
            i = find(i)
            j = find(j)
            if i == j:
                return
            if height[i] > height[j]:
                parent[j] = i
            elif height[i] < height[j]:
                parent[i] = j
            else:
                parent[i] = j
                height[j] += 1

        n = len(accounts)
        parent = list(range(n))
        height = [0] * n
        email2i = dict()
        i2emails = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in email2i:
                    email2i[email] = i
                else:
                    union(i, email2i[email])
        for email, i in email2i.items():
            i2emails[find(i)].append(email)
        for emails in i2emails.values():
            emails.sort()
        return [[accounts[k][0]] + v for k, v in i2emails.items()]


print(Solution().accountsMerge([["Hanzo", "Hanzo2@m.co", "Hanzo3@m.co"], ["Hanzo", "Hanzo4@m.co", "Hanzo5@m.co"],
                                ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo4@m.co"],
                                ["Hanzo", "Hanzo7@m.co", "Hanzo8@m.co"], ["Hanzo", "Hanzo1@m.co", "Hanzo2@m.co"],
                                ["Hanzo", "Hanzo6@m.co", "Hanzo7@m.co"], ["Hanzo", "Hanzo5@m.co", "Hanzo6@m.co"]]))
