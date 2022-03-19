from heapq import heappop, heapify, heappush
from collections import deque


def GetFirstDiceRollOfBestSequence(cells: [int]):
    pq = []
    cells = [0] + cells
    n = len(cells)
    predecessor = [None] * n
    dist = [float('inf')] * n
    seen = [0] * n
    for i in range(1, 7):
        i %= n
        pq.append((cells[i], i))
        dist[i] = cells[i]
        predecessor[i] = 0
    heapify(pq)
    while True:
        cost, cell = heappop(pq)
        while seen[cell]:
            cost, cell = heappop(pq)
        seen[cell] = 1
        if cell == 0:
            break
        for i in range(cell + 1, cell + 7):
            i %= n
            if seen[i] == 0 and dist[i] > cost + cells[i]:
                dist[i] = cost + cells[i]
                predecessor[i] = cell
                heappush(pq, (dist[i], i))
    i = 0
    while predecessor[i] != 0:
        i = predecessor[i]
    return i


def GetFirstDiceRollOfBestSequence1(cells: [int]):
    n = len(cells)
    if n < 6:
        return 0
    window_min = deque()
    for i in range(n - 1, n - 7, -1):
        while window_min and cells[window_min[-1]] > cells[i]:
            window_min.pop()
        window_min.append(i)
    for i in range(n - 7, -1, -1):
        cells[i] += cells[window_min[0]]
        if window_min[0] == i + 6:
            window_min.popleft()
        while window_min and cells[window_min[-1]] > cells[i]:
            window_min.pop()
        window_min.append(i)
    return window_min[0] + 1


print(GetFirstDiceRollOfBestSequence([1, 7, 3, 4, 2, 6, 6]))
