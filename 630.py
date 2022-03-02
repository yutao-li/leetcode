from heapq import heappush, heapreplace
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        max_heap = []
        timestamp = 0
        count = 0
        for i, j in courses:
            if timestamp + i <= j:
                count += 1
                heappush(max_heap, -i)
                timestamp += i
            elif max_heap and -max_heap[0] > i:
                timestamp -= -max_heap[0] - i
                heapreplace(max_heap, -i)
        return count


print(Solution().scheduleCourse(
    courses=[[7, 16], [2, 3], [3, 12], [3, 14], [10, 19], [10, 16], [6, 8], [6, 11], [3, 13], [6, 16]]))
