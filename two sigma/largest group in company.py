from collections import defaultdict


def solution(relations: [int, int, int]) -> [int]:
    def dfs(i):
        seen.add(i)
        cur_group.append(i)
        for j in adj[i]:
            if j not in seen:
                dfs(j)

    company = defaultdict(list)
    for a, b, c in relations:
        company[c].append([a, b])
    res = []
    for pairs in company.values():
        adj = defaultdict(list)
        for a, b in pairs:
            adj[a].append(b)
            adj[b].append(a)
        people = list(adj.keys())
        seen = set()
        for i in people:
            if i not in seen:
                cur_group = []
                dfs(i)
                if len(cur_group) > len(res):
                    res = cur_group
    return res


print(solution([[1, 2, 1], [2, 3, 1]]))
