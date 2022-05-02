class Graph:
    def __init__(self, edges, numNode):
        self.numNode = numNode
        self.adjList = [[] for _ in range(numNode)]
        for a, b in edges:
            self.adjList[a].append(b)
            self.adjList[b].append(a)


class Diffusion:
    def __init__(self, graph):
        self.graph = graph
        self.values = [0] * graph.numNode
        self.diffused = set()

    def trigger(self, node, value):
        if value == self.values[node]:
            return
        self.values[node] = value
        self.diffused = {node}

    def step(self):
        if not self.diffused:
            raise RuntimeError('not initiated or completed')
        nextDiffused = set()
        for node in self.diffused:
            neighbours = self.graph.adjList[node]
            avg = (sum(self.values[i] for i in neighbours) + self.values[node]) / (len(neighbours) + 1)
            self.values[node] = avg
            for n in neighbours:
                if self.values[n] != avg:
                    self.values[n] = avg
                    nextDiffused.add(n)
        self.diffused = nextDiffused
        return bool(nextDiffused)


edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
graph = Graph(edges, 5)
diffusion = Diffusion(graph)
diffusion.trigger(2, 10)
diffusion.step()
print(diffusion.values)
diffusion.step()
print(diffusion.values)
diffusion.step()
print(diffusion.values)
