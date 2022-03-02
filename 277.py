# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass


class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        for i in range(1, n):
            if knows(celebrity, i):
                celebrity = i
        if any(knows(celebrity, i) or not knows(i, celebrity) for i in range(celebrity)):
            return -1
        if any(not knows(i, celebrity) for i in range(celebrity + 1, n)):
            return -1
        return celebrity
