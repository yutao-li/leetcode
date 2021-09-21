from collections import Counter


def stockPairs(stocksProfit, target):
    stocksProfit = Counter(stocksProfit)
    res = 0
    if target % 2 == 0 and stocksProfit[target / 2] > 1:
        res += 1
        del stocksProfit[target / 2]
    log = set()
    for n in stocksProfit:
        if target - n in log:
            res += 1
        else:
            log.add(n)
    return res


print(stockPairs(list(range(10)), 8))
