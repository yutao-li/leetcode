class TwoSum:

    def __init__(self):
        self.arr = set()
        self.sums = set()

    def add(self, number: int) -> None:
        if number in self.arr:
            self.sums.add(number * 2)
        else:
            for i in self.arr:
                self.sums.add(i + number)
            self.arr.add(number)

    def find(self, value: int) -> bool:
        return value in self.sums

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
