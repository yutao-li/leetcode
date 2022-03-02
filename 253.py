from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)
        j = 0
        room = 0
        for s in start:
            if s >= end[j]:
                j += 1
            else:
                room += 1
        return room


res = Solution().minMeetingRooms([[7, 10], [2, 4]])
