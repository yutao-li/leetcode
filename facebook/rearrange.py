def solution(s: str) -> str:
    h, r = divmod(len(s), 2)
    res = ''
    for i in range(h):
        res += s[i] + s[-i - 1]
    if r:
        res += s[h]
    return res


print(solution('abcdef'))
print(solution('abcde'))
