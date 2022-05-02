def probabilityOfWin(n, mn, mx):
    if mx - mn + 1 >= n:
        return 1
    dp = [1] * (mx - mn + 1) + [0] * (n - (mx - mn + 1))
    iteration, start = divmod(mn, n)
    if start:
        iteration += 1
    winProbSum = (mx - mn + 1)
    for _ in range(iteration):
        for i in range(n - 1, -1, -1):
            tmp = winProbSum / n
            winProbSum += tmp - dp[i]
            dp[i] = tmp
    return dp[-start]


print(probabilityOfWin(10, 40, 44))
