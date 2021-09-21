class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        la = []
        lb = []
        for a, b in zip(A, B):
            if a != b:
                la.append(a)
                lb.append(b)
        queue = {''.join(la): 0}
        while lb:
            q = {}
            for pre, swap in queue.items():
                if pre[-1] != lb[-1]:
                    eq = []
                    for i, ch in enumerate(pre[:-1]):
                        if ch == lb[-1] and lb[i] != ch:
                            eq.append(i)
                            if lb[i] == pre[-1]:
                                eq = [i]
                                break
                    for i in eq:
                        tmp = pre[:i] + pre[-1] + pre[i + 1:-1]
                        q[tmp] = min(swap + 1, q.get(tmp, float('inf')))
                else:
                    q[pre[:-1]] = min(swap, q.get(pre[:-1], float('inf')))
            lb.pop()
            queue = q
        return list(queue.values())[0]
