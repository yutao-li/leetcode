from string import ascii_lowercase, ascii_uppercase


def transform(s: str):
    vowels = 'aeiou'
    cl = [i for i in ascii_lowercase if i not in vowels]
    ch = [i for i in ascii_uppercase if i not in vowels.upper()]
    map = dict(zip(cl, cl[1:] + ['b']))
    map.update(zip(ch, ch[1:] + ['B']))
    return ''.join(map.get(ch, ch) for ch in s)


print(transform("CodeSignal"))
