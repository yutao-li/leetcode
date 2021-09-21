import sys
from collections import defaultdict

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    courses = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        courses.append(list(map(int, line.split())))
    courses.sort(key=lambda x: x[1])
    finish = [c[1] for c in courses]
    di = defaultdict(list)
    for i, c in enumerate(courses):
        di[c[0]].append(i)
    start = sorted(di.keys())
    pre = [0] * len(courses)
    cur = -1
    for s in start:
        while finish[cur + 1] <= s:
            cur += 1
        for i in di[s]:
            pre[i] = cur

    dp = [0] * len(courses)
    dp[0] = courses[0][2]
    for i in range(1, len(courses)):
        dp[i] = max(dp[i - 1], courses[i][2] + (dp[pre[i]] if pre[i] != -1 else 0))
    print(dp[-1])
