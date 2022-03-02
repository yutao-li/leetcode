from functools import lru_cache


def solution(deps: [[int]], n: int):
    @lru_cache(None)
    def dfs(state):
        return 1 + max([dfs(state | adj[i]) for i in range(n) if bin_rep[i] & state == 0], default=-1)

    bin_rep = [1 << i for i in range(n)]
    adj = bin_rep[:]
    for a, b in deps:
        adj[a] |= bin_rep[b]
        adj[b] |= bin_rep[a]
    return dfs(0)


deps = [[0, 1], [2, 3], [2, 4]]
print(solution(deps, 5))
