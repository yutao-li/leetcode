from random import randrange


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.pos = dict()

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        i = self.pos[val]
        last = self.nums[-1]
        self.nums[i] = last
        self.pos[last] = i
        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return self.nums[randrange(len(self.nums))]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
