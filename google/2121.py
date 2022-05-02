class VersionRange:
    def __init__(self, minVersion=None, maxVersion=None):
        self.minVersion = minVersion
        self.maxVersion = maxVersion


def divideVersionsIntoIntervals(versions: [VersionRange]) -> [VersionRange]:
    if not versions:
        return []
    bounds = set()
    for versionRange in versions:
        if versionRange.minVersion:
            bounds.add(versionRange.minVersion - 1)
        if versionRange.maxVersion:
            bounds.add(versionRange.maxVersion)
    bounds = sorted(bounds)
    start = -1
    res = []
    for b in bounds:
        res.append(VersionRange(start, b))
        start = b + 1
    res.append(VersionRange(start, 1000))
    return res


vrs = divideVersionsIntoIntervals([VersionRange(4, 7), VersionRange(None, 16), VersionRange(7, 10)])
for vr in vrs:
    print(vr.minVersion, vr.maxVersion)
