from heapq import heapify, heappop, heappush
from random import random, randrange
from string import ascii_lowercase


class HuffmanTree:
    def __init__(self, chars: [str], frequencies: [int]):
        def dfs(prefix, tree):
            if isinstance(tree, str):
                self.encoding[tree] = prefix
            else:
                dfs(prefix + '0', tree[0])
                dfs(prefix + '1', tree[1])

        pq = [(f, ch) for ch, f in zip(chars, frequencies)]
        heapify(pq)
        while len(pq) > 1:
            f1, tree1 = heappop(pq)
            f2, tree2 = heappop(pq)
            heappush(pq, (f1 + f2, [tree1, tree2]))
        self.tree = pq[0][1]
        self.encoding = dict()
        dfs('', self.tree)

    def encode(self, s: str) -> str:
        return ''.join(self.encoding[ch] for ch in s)

    def decode(self, s: str) -> str:
        res = []
        tree = self.tree
        for bit in s:
            if isinstance(tree, str):
                res.append(tree)
                tree = self.tree
            tree = tree[int(bit)]
        res.append(tree)
        return ''.join(res)


for _ in range(100):
    frequencies = [random() for _ in range(26)]
    ht = HuffmanTree(ascii_lowercase, frequencies)
    s = ''.join(ascii_lowercase[randrange(26)] for _ in range(10))
    encoded = ht.encode(s)
    decoded = ht.decode(encoded)
    assert s == decoded, s + ' ' + decoded
