def solution(segments: [int]) -> int:
    start_order = sorted(i for i, _ in segments)
    end_order = sorted(i for _, i in segments)
    start = 1
    res = 0
    n = len(segments)
    for i in end_order:
        while start < n and start_order[start] < i:
            start += 1
        if start == n:
            break
        res += n - start
    return res


segments = [[0, 3], [2, 8], [3, 7], [5, 14], [6, 8], [6, 10], [9, 14], [10, 12], [10, 16], [12, 14]]
print(solution(segments))
