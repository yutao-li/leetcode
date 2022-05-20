from collections import defaultdict


def findNearestCafeterias(friends, cafeterias, edges):
    adjList = defaultdict(list)
    for a, b in edges:
        adjList[a].append(b)
        adjList[b].append(a)
    n = len(friends)
    seen = [{f} for f in friends]
    pools = [[f] for f in friends]
    counter = {c: 0 for c in cafeterias}
    for f in friends:
        if f in counter:
            counter[f] += 1
    while all(pools):
        for i, pool in enumerate(pools):
            newPool = []
            for location in pool:
                for neighbor in adjList[location]:
                    if neighbor not in seen[i]:
                        seen[i].add(neighbor)
                        newPool.append(neighbor)
                        if neighbor in counter:
                            counter[neighbor] += 1
                            if counter[neighbor] == n:
                                return neighbor
            pools[i] = newPool
    return -1


print(findNearestCafeterias([1], [5], [(1, 2), (1, 3), (2, 4)]))
print(findNearestCafeterias([1], [5], [(1, 5)]))
print(findNearestCafeterias([1], [5, 7], [(1, 2), (1, 3), (2, 4), (2, 7)]))
print(findNearestCafeterias([1, 2], [1, 3], [(1, 3), (2, 3)]))
print(findNearestCafeterias([1, 2, 3], [5, 6, 7, 8, 9],
                            [(1, 2), (1, 10), (10, 8), (2, 11), (2, 6), (3, 7), (8, 6), (7, 8)]))
