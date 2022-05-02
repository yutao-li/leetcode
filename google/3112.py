def getPredicate(s):
    if not s:
        return 'False'
    return ' or '.join('x==' + str(i) for i in s)


def getIntervals(s):
    intervals = []
    for i in s:
        if intervals and intervals[-1][1] + 1 == i:
            intervals[-1][1] += 1
        else:
            intervals.append([i, i])
    return intervals


def intervalToPredicate(interval):
    i, j = interval
    return 'x==' + str(i) if i == j else str(i) + '<=x<=' + str(j)


def getPredicateWithInterval(s):
    if not s:
        return 'False'
    s = sorted(s)
    intervals = getIntervals(s)
    return ' or '.join(intervalToPredicate(interval) for interval in intervals)


def getBstPredicate(s):
    def getBstPredicateOfIntervals(intervals):
        if len(intervals) == 1:
            return intervalToPredicate(intervals[0])
        mid = len(intervals) // 2
        boundary = str(intervals[mid][0])
        return 'x<' + boundary + ' and (' + getBstPredicateOfIntervals(
            intervals[:mid]) + ') or x>=' + boundary + ' and (' + getBstPredicateOfIntervals(intervals[mid:]) + ')'

    intervals = getIntervals(s)
    return getBstPredicateOfIntervals(intervals)


print(getPredicate({1, 2}))
print(getPredicateWithInterval({1, 2, 3, 5}))
print(getBstPredicate({1, 2, 6, 7, 8, 15, 16, 19}))
