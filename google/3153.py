def probabilityOfWin(n, mn, mx):
    if mx - mn + 1 >= n:
        return 1
    dp = [0] * (n - (mx - mn + 1)) + [1] * (mx - mn + 1)
    winProbSum = (mx - mn + 1)
    for i in range(mn):
        tmp = winProbSum / n
        winProbSum += tmp - dp[i % n]
        dp[i % n] = tmp
    return dp[(mn - 1) % n]


print(probabilityOfWin(10, 40, 44))
