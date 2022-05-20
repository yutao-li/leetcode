from functools import cache


@cache
def getBeautyByValue(n, k, c, blockColors):
    maxValue = 0
    curValue = 0
    for color in blockColors:
        if color == c:
            curValue += 1
        else:
            maxValue = max(maxValue, curValue)
            curValue = 0
    return max(maxValue, curValue)


def getBeautyByValues(n, k, favoriteColors, blockColors):
    return [getBeautyByValue(n, k, c, blockColors) for c in favoriteColors]


@cache
def getMaximumBeautyValue(n, k, c, m, blockColors):
    left = right = 0
    maxValue = 0
    while right < n:
        if blockColors[right] != c:
            if m > 0:
                m -= 1
            else:
                maxValue = max(maxValue, right - left)
                while blockColors[left] == c:
                    left += 1
                left += 1
        right += 1
    return max(maxValue, right - left)


def getMaximumBeautyValues(n, k, ms, favoriteColors, blockColors):
    return [getMaximumBeautyValue(n, k, c, m, blockColors) for m, c in zip(ms, favoriteColors)]


def getMaximumBeautyValueCircular(n, k, c, m, blockColors):
    numDiff = sum(i != c for i in blockColors)
    if numDiff <= m:
        return n
    return getMaximumBeautyValue(2 * n, k, c, m, blockColors * 2)
