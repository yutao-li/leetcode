def solution(strings: [str], sources: [str]) -> [bool]:
    prefix = dict()
    i = 0
    cur = ''
    for s in strings:
        i += len(s)
        cur += s
        prefix[i] = cur
    return [prefix.get(len(s), '') == s for s in sources]


strings = ['one', 'two', 'three']
sources = ['onetwo', 'one']
print(solution(strings, sources))
strings = ['one', 'twothree', 'four']
sources = ['one', 'onetwo']
print(solution(strings, sources))
