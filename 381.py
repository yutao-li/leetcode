from random import randrange


class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.pos = dict()
        self.count = dict()

    def insert(self, val: int) -> bool:
        if val in self.count:
            c = self.count[val]
            self.nums.append((val, c))
            self.pos[val, c] = len(self.nums) - 1
            self.count[val] += 1
            return False
        else:
            self.count[val] = 1
            self.nums.append((val, 0))
            self.pos[val, 0] = len(self.nums) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.count:
            return False
        self.count[val] -= 1
        c = self.count[val]
        if c == 0:
            del self.count[val]
        last = self.nums[-1]
        i = self.pos[val, c]
        self.nums[i] = last
        self.pos[last] = i
        self.nums.pop()
        del self.pos[val, c]
        return True

    def getRandom(self) -> int:
        return self.nums[randrange(len(self.nums))][0]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
