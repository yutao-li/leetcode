def minStringCoeff(s, p):
    # Write your code here
    begin = 1
    end = len(s) - 2
    while begin < len(s) and s[begin] == s[begin - 1]:
        begin += 1
    if begin == len(s):
        return 0
    while s[end] == s[end + 1]:
        end -= 1
    seg = []
    while begin <= end:
        i = begin + 1
        while s[i] == s[i - 1]:
            i += 1
        seg.append(i - begin)
        begin = i
    if p > (len(seg) - 1) // 2:
        return 0
    width = len(seg) - 2 * p
    mini = sum(seg[:width])
    cur = sum(seg[:width])
    for i in range(width, len(seg)):
        cur += seg[i] - seg[i - width]
        if cur < mini:
            mini = cur
    return mini


res = minStringCoeff('000111', 0)
