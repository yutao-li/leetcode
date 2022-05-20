from collections import defaultdict


class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2


class Graph:
    def __init__(self, edges: [Edge]):
        self.edges = edges


def buildGridGraph(n: int, m: int) -> Graph:
    edges = []
    for i in range(n):
        for j in range(m):
            v = m * i + j
            if j < m - 1:
                edges.append([v, v + 1])
            if i < n - 1:
                edges.append([v, v + m])
    return Graph(edges)


def isValid33(graph: Graph) -> bool:
    if len(graph.edges) != 12:
        return False
    adj = defaultdict(list)
    for a, b in graph.edges:
        adj[a].append(b)
        adj[b].append(a)
    degree = defaultdict(list)
    for v, n in adj.items():
        degree[len(n)].append(v)
    if not (len(degree[2]) == 4 and len(degree[3]) == 4 and len(degree[4]) == 1):
        return False
    center = degree[4][0]
    if set(degree[3]) != set(adj[center]):
        return False
    for v in degree[3]:
        adj[v].remove(center)
    cur = degree[2][0]
    pre = -1
    seen = set()
    for i in range(8):
        if i % 2 == 0:
            if cur not in degree[2]:
                return False
        else:
            if cur not in degree[3]:
                return False
        a, b = adj[cur]
        if a == pre:
            cur, pre = b, cur
        else:
            cur, pre = a, cur
        seen.add(cur)
    if seen != set(degree[2] + degree[3]):
        return False
    return True


def isGridGraphValid(graph: Graph, row: int, column: int) -> bool:
    def isLine(adj: {{int}}, length: int) -> bool:
        if len(adj) != length:
            return False
        degree2count = defaultdict(list)
        for v, n in adj.items():
            degree2count[len(n)].append(v)
        if not (len(degree2count[1]) == 2 and len(degree2count[2]) == length - 2):
            return False
        start, end = degree2count[1]
        for i in range(length - 1):
            neighbours = adj[start]
            if i and len(neighbours) != 2:
                return False
            a, b = neighbours
            if a == start:
                start = b
            else:
                start = a
        return start == end

    def isValid(adj: {{int}}, row: int, column: int) -> bool:
        if row == 0:
            return not bool(adj)
        if row == 1:
            return isLine(adj, column)
        degree2count = defaultdict(int)
        for v, n in adj.items():
            degree2count[len(n)] += 1
        if not (degree2count[0] == 4 and degree2count[3] == 2 * (row - 2 + column - 2) and degree2count[4] == (
                column - 2) * (row - 2)):
            return False

    if row > column:
        row, column = column, row
    if len(graph.edges) != (column - 1) * row + (row - 1) * column:
        return False
    vertices = set(i for edge in graph.edges for i in edge)
    if len(vertices) != row * column:
        return False
    adj = defaultdict(set)
    for a, b in graph.edges:
        adj[a].add(b)
        adj[b].add(a)
    return isValid(adj, row, column)


print(isValid33(buildGridGraph(3, 3)))
