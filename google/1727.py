from string import ascii_letters
from random import shuffle


def getRing(graph):
    if len(graph) <= 2:
        return list(graph)
    pre = None
    cur = next(iter(graph))
    n = len(graph)
    ring = [cur]
    for _ in range(n - 1):
        node1, node2 = graph[cur]
        if node1 != pre:
            pre, cur = cur, node1
        else:
            pre, cur = cur, node2
        ring.append(cur)
    return ring


def checkAndGetRing(graph):
    if not graph:
        raise AssertionError('empty graph')
    elif len(graph) == 1:
        node = next(iter(graph))
        assert [node] == graph[node], "not a valid self ring"
        return [node]
    elif len(graph) == 2:
        n1, n2 = graph
        assert graph[n1] == [n2] and graph[n2] == [n1], "not a valid two-node ring"
        return [n1, n2]
    pre = None
    cur = next(iter(graph))
    n = len(graph)
    ring = [cur]
    for i in range(n):
        assert len(graph[cur]) == 2, "num of neighbours of " + cur + " is not 2"
        node1, node2 = graph[cur]
        assert not pre or node1 == pre or node2 == pre, "neighbours of " + cur + " not contains previous node " + pre
        if node1 != pre:
            pre, cur = cur, node1
        else:
            pre, cur = cur, node2
        assert i == n - 1 or cur != ring[0], "head node " + ring[0] + " is revisited before visiting all nodes"
        ring.append(cur)
    assert ring[0] == ring[-1], "ring doesn't cover all nodes"
    ring.pop()
    return ring


nodes = list(ascii_letters)
n = len(nodes)
for _ in range(10):
    shuffle(nodes)
    graph = {j: [i, k] for i, j, k in zip([nodes[-1]] + nodes, nodes, nodes[1:] + [nodes[0]])}
    print(checkAndGetRing(graph))

try:
    graph = {'a': ['b']}
    checkAndGetRing(graph)
    raise ValueError('graph should be invalid')
except AssertionError as e:
    assert str(e) == "not a valid self ring"

try:
    graph = {'a': ['b'], 'b': ['b']}
    checkAndGetRing(graph)
    raise ValueError('graph should be invalid')
except AssertionError as e:
    assert str(e) == "not a valid two-node ring"

try:
    graph = {'a': ['b'], 'b': ['a', 'c'], 'c': ['a', 'b']}
    checkAndGetRing(graph)
    raise ValueError('graph should be invalid')
except AssertionError as e:
    assert str(e) == "num of neighbours of a is not 2"
