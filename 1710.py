from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        i = 0
        len_types = len(boxTypes)
        res = 0
        while truckSize > 0 and i < len_types:
            num_box, num_unit = boxTypes[i]
            num_load = min(num_box, truckSize)
            res += num_load * num_unit
            truckSize -= num_load
            i += 1
        return res
