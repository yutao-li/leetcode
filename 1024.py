from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key=lambda x: x[0])
        left = 0
        i = 0
        res = 0
        while left < T:
            right = left
            while i < len(clips) and clips[i][0] <= left:
                right = max(right, clips[i][1])
                i += 1
            if right == left:
                return -1
            res += 1
            left = right
        return res


print(Solution().videoStitching([[0,4],[2,8]], 5))
