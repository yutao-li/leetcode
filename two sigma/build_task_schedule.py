from collections import defaultdict


def solution(codebase2time: {str: int}, dependency: {str: [str]}) -> [int, [str]]:
    in_degree = {k: len(v) for k, v in dependency.items()}
    unblock = defaultdict(list)
    for k, v in dependency.items():
        for i in v:
            unblock[i].append(k)
    res = []
    n = len(codebase2time)
    pool = [i for i in codebase2time if i not in in_degree]
    seen = 0
    while seen < n:
        if not pool:
            return []
        duration = min(codebase2time[i] for i in pool)
        remain = []
        for i in pool:
            if codebase2time[i] > duration:
                codebase2time[i] -= duration
                remain.append(i)
            else:
                seen += 1
                for j in unblock[i]:
                    in_degree[j] -= 1
                    if in_degree[j] == 0:
                        remain.append(j)
        res.append([duration, pool])
        pool = remain
    return res


codebase2time = {"A": 1, "B": 3, "C": 2, "D": 2, "E": 4}
dependency = {
    "B": ["A"],
    "C": ["A"],
    "D": ["B", "C"],
    "E": ["A", "C"]
}
print(solution(codebase2time, dependency))
