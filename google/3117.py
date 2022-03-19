from collections import defaultdict


def isGridGraphValid(graph: [[int, int]], row: int, column: int) -> bool:
    vertices = set(i for edge in graph for i in edge)
    if len(vertices) != row * column:
        return False
    adj = defaultdict(list)
    for a, b in graph:
        adj[a].append(b)
        adj[b].append(a)
    corners = [k for k, v in adj.items() if len(v) == 2]
    if len(corners) != 4:
        return False
    pool = []
    for vertex in corners:
        n1, n2 = adj[vertex]
        if not (len(adj[n1]) == 3 and len(adj[n2]) == 3):
            return False
        pool.append(n1)
        pool.append(n2)
   