# https://www.careercup.com/question?id=5759582094229504
from functools import reduce
from typing import List


class Array:
    array = [[[i + j + 1, i + j + 2, i + j + 3] for i in range(4)] for j in range(5)]

    def getDim(self) -> List[int]:
        return [5, 4, 3]

    def getElement(self, indices: List[int]) -> int:
        arr = Array.array
        for i in indices:
            arr = arr[i]
        return arr


def sum_all(array: Array) -> int:
    dim = array.getDim()
    n = len(dim)
    index = [0] * n
    index[-1] = -1
    total = reduce(lambda x, y: x * y, dim)
    res = 0
    for _ in range(total):
        j = n - 1
        index[j] += 1
        while index[j] == dim[j]:
            index[j] = 0
            j -= 1
            index[j] += 1
        res += array.getElement(index)
    return res


print(sum_all(Array()))
print(sum(Array.array[i][j][k] for i in range(5) for j in range(4) for k in range(3)))
