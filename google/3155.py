from collections import defaultdict


def arrangeKnockout(country2teams, groups, N):
    def findRival(team):
        existing = countrymatched[team]
        candidates = adjList[team]
        for c in candidates:
            if c not in existing:
                return c
        return candidates[0]

    def removeNode(n):
        for n1 in adjList[n]:
            adjList[n1].remove(n)
            if not adjList[n1]:
                del adjList[n1]
        del adjList[n]

    groups += list(country2teams.values())
    countrymatched = defaultdict(set)
    disjointList = [[] for _ in range(N)]
    for group in groups:
        for i, team in enumerate(group):
            disjointList[team] += group[:i] + group[i + 1:]
    adjList = defaultdict(list)
    for team, excluded in enumerate(disjointList):
        adjList[team] = [t for t in range(N) if t not in set(excluded)]
    matched = []
    while adjList:
        pick = None
        for k, v in adjList.items():
            if len(v) == 1:
                pick = k
                break
        if not pick:
            pick = next(iter(adjList))
        rival = findRival(pick)
        countrymatched[rival].add(pick)
        countrymatched[pick].add(rival)
        removeNode(pick)
        removeNode(rival)
        matched.append([pick, rival])
    return matched
