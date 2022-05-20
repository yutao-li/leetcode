from functools import reduce


def numOfDistinctPaths(width, height):
    dp = [0] * (height - 1) + [1]
    for _ in range(width - 1):
        dp = [sum(triplet) for triplet in zip([0] + dp, dp, dp[1:] + [0])]
    return dp[-1]


def pathsBetweenTwoTargets(target1, target2, height):
    x1, y1 = target1
    x2, y2 = target2
    if x1 >= x2:
        return 0
    dp = [0] * height
    dp[y2] = 1
    for _ in range(x2 - x1):
        dp = [sum(triplet) for triplet in zip([0] + dp, dp, dp[1:] + [0])]
    return dp[y1]


def numOfDistinctPathsThroughOrderedTargets(width, height, orderedTargets):
    return reduce(lambda x, y: x * y, [pathsBetweenTwoTargets(target1, target2, height) for target1, target2 in
                                       zip([(0, 0)] + orderedTargets, orderedTargets + [(width - 1, 0)])])


def numOfDistinctPathsThroughUnorderedTargets(width, height, unorderedTargets):
    return numOfDistinctPathsThroughOrderedTargets(width, height, sorted(unorderedTargets))


def numOfDistinctPathsThroughUnorderedTargetsWithBlockers(width, height, unorderedTargets, blockers):
    def pathsBetweenTwoTargets(target1, target2):
        x1, y1 = target1
        x2, y2 = target2
        if x1 >= x2:
            return 0
        dp = [0] * height
        dp[y2] = 1
        for x in range(x2, x1, -1):
            for y in xBlockers[x]:
                dp[y] = 0
            dp = [sum(triplet) for triplet in zip([0] + dp, dp, dp[1:] + [0])]
        return dp[y1]

    xBlockers = [[] for _ in range(width)]
    for x, y in blockers:
        xBlockers[x].append(y)
    unorderedTargets.sort()
    return reduce(lambda x, y: x * y, [pathsBetweenTwoTargets(target1, target2) for target1, target2 in
                                       zip([(0, 0)] + unorderedTargets, unorderedTargets + [(width - 1, 0)])])


print(numOfDistinctPaths(4, 5))
print(numOfDistinctPathsThroughOrderedTargets(4, 5, []))
