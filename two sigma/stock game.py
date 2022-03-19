def solution(prices: [int], day: int) -> int:
    n = len(prices)
    forward = [-1] * n
    backward = [-1] * n
    stack = []
    for i, p in enumerate(prices):
        while stack and p < prices[stack[-1]]:
            top = stack.pop()
            forward[top] = i
        stack.append(i)
    stack = []
    for i, p in enumerate(prices[::-1]):
        i = n - 1 - i
        while stack and p < prices[stack[-1]]:
            top = stack.pop()
            backward[top] = i
        stack.append(i)
    if forward[day] == -1:
        return backward[day]
    if backward[day] == -1:
        return forward[day]
    if forward[day] - day > day - backward[day]:
        return forward[day]
    else:
        return backward[day]
