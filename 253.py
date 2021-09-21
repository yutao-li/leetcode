from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)
        i = 0
        j = 0
        room = 0
        while i < len(intervals):
            if start[i] >= end[j]:
                j += 1
            else:
                room += 1
            i += 1
        return room


res = Solution().minMeetingRooms([[7,10],[2,4]])
