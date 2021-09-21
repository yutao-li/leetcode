from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        es = set()
        for email in emails:
            p1 = email.find('@')
            user = email[:p1]
            p2 = user.find('+')
            if p2 != -1:
                user = user[:p2]
            user = user.replace('.', '')
            es.add(user + email[p1:])
        return len(es)

print(Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))