from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        aver, r = divmod(total, len(machines))
        if r:
            return -1
        move = 0
        machines = [i for i in machines if i != aver]
        while machines:
            if machines[0] > aver and machines[0] > machines[1]:
                machines[0] -= 1
                machines[1] += 1
            if machines[-1] > aver and machines[-1] > machines[-2]:
                machines[-1] -= 1
                machines[-2] += 1
            i = 1
            left_sum, right_sum = machines[0], sum(machines[2:])
            while i < len(machines) - 1:
                forward = left_sum / i > right_sum / (len(machines) - i - 1)
                feasi = machines[i] > machines[i + 1] if forward else machines[i] > machines[i - 1]
                if feasi:
                    if forward:
                        machines[i] -= 1
                        machines[i + 1] += 1
                    else:
                        machines[i] -= 1
                        machines[i - 1] += 1
                left_sum += machines[i] + (not forward and feasi)
                right_sum -= machines[i + 1] - (forward and feasi)
                i += 1
            move += 1
            machines = [i for i in machines if i != aver]
        return move


print(Solution().findMinMoves([44, 46, 11, 2, 12, 64, 40, 60, 92, 9]))
