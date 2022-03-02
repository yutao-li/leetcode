from collections import defaultdict


def solution(queries: [str], diff: int) -> [int]:
    count = defaultdict(int)
    res = []
    cur = 0
    for q in queries:
        n = int(q[1:])
        if q[0] == '+':
            cur += count[n - diff] + count[n + diff]
            count[n] += 1
        else:
            cur -= count[n] * (count[n - diff] + count[n + diff])
            del count[n]
        res.append(cur)
    return res


queries = ['+4', '+5', '+2', '-4']
print(solution(queries, 1))
queries = ['+2', '+2', '+4', '+3', '-2']
print(solution(queries, 1))
