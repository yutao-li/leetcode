class Solution:
    def __init__(self):
        self.memory = []

    def malloc(self, size: int) -> int:
        i = 0
        pre_ptr = -1
        while i < len(self.memory):
            if self.memory[i + 1] == 0 and self.memory[i] >= size + 3:
                if self.memory[i] > size + 6:
                    j = i + size + 3
                    k = i + self.memory[i]
                    self.memory[j] = self.memory[i] - size - 3
                    self.memory[j + 1] = 0
                    self.memory[j + 2] = i
                    self.memory[i] = size + 3
                    if k < len(self.memory):
                        self.memory[k + 2] = j
                self.memory[i + 1] = 1
                break
            else:
                pre_ptr = i
                i += self.memory[i]
        if i == len(self.memory):
            self.memory += [size + 3, 1, pre_ptr] + [0] * size
        return i

    def free(self, ptr: int):
        self.memory[ptr + 1] = 0
        next_ptr = ptr + self.memory[ptr]
        if next_ptr < len(self.memory) and self.memory[next_ptr + 1] == 0:
            self.memory[ptr] += self.memory[next_ptr]
            next_next_ptr = next_ptr + self.memory[next_ptr]
            if next_next_ptr < len(self.memory):
                self.memory[next_next_ptr + 2] = ptr
        if ptr != 0:
            pre_ptr = self.memory[ptr + 2]
            if self.memory[pre_ptr + 1] == 0:
                self.memory[pre_ptr] += self.memory[ptr]
                next_ptr = ptr + self.memory[ptr]
                if next_ptr < len(self.memory):
                    self.memory[next_ptr + 2] = pre_ptr


m = Solution()
m.malloc(3)
m.malloc(4)
m.malloc(6)
m.malloc(2)
m.malloc(3)
m.malloc(2)
m.free(7 + 6)
m.malloc(3)
m.free(13 + 9)
m.free(18 + 15)
m.free(15 + 12)
print(m.memory)
