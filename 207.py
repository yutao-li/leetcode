from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def take(course):
            taken[course] = 2
            for pre_course in prereq[course]:
                if taken[pre_course] == 0:
                    if not take(pre_course):
                        return False
                elif taken[pre_course] == 2:
                    return False
            taken[course] = 1
            return True

        prereq = defaultdict(list)
        for i, j in prerequisites:
            prereq[i].append(j)
        taken = [0] * numCourses

        for i in range(numCourses):
            if not taken[i]:
                if not take(i):
                    return False
        return True
