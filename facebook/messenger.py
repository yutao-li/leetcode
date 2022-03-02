def solution(messages, width, userWidth):
    def align(m, u):
        if u == '1':
            return m + ' ' * (width - len(m))
        else:
            return ' ' * (width - len(m)) + m

    res = ['+' + '*' * width + '+']
    for u, m in messages:
        i = 0
        lm = len(m)
        while i < lm:
            j = i + userWidth
            if j >= lm:
                res.append('|' + align(m[i:], u) + '|')
                break
            else:
                if m[j - 1:j + 1].isalpha():
                    j -= 1
                    while m[j - 1].isalpha():
                        j -= 1
                res.append('|' + align(m[i:j], u) + '|')
                i = j
            while i < lm and m[i] == ' ':
                i += 1
    res.append(res[0])
    return res


messages = [['1', 'Hello how r u'], ['2', 'good ty'], ['2', 'u'], ['1', 'me too bro']]
for line in solution(messages, 15, 5):
    print(line)
