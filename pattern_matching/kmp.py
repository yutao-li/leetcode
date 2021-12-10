from typing import List


def full_dfa_kmp(text: str, pattern: str) -> int:
    text = [ord(i) for i in text]
    pattern = [ord(i) for i in pattern]
    dfa: List[List[int]] = [[0] * 128]
    dfa[0][pattern[0]] = 1
    state = 0
    for i in range(1, len(pattern)):
        dfa.append(list(dfa[state]))
        dfa[-1][pattern[i]] = i + 1
        state = dfa[state][pattern[i]]
    j = 0
    for i, ch in enumerate(text):
        j = dfa[j][ch]
        if j == len(pattern):
            return i - len(pattern) + 1
    return -1


def multi_match_kmp(text: str, pattern: str) -> List[int]:
    res = []
    text = [ord(i) for i in text]
    pattern = [ord(i) for i in pattern]
    dfa: List[List[int]] = [[0] * 128]
    dfa[0][pattern[0]] = 1
    state = 0
    for i in range(1, len(pattern)):
        dfa.append(list(dfa[state]))
        dfa[-1][pattern[i]] = i + 1
        state = dfa[state][pattern[i]]
    dfa.append(list(dfa[state]))
    j = 0
    for i, ch in enumerate(text):
        j = dfa[j][ch]
        if j == len(pattern):
            res.append(i - len(pattern) + 1)
    return res


PATTERN = 'NEEDLE'
TEXT = 'INAHAYSTACKNEEDLEINA'
print(full_dfa_kmp(TEXT, PATTERN) == TEXT.find(PATTERN))

TEXT = 'ABACADABRAC'
PATTERN = 'ABRA'
print(full_dfa_kmp(TEXT, PATTERN) == TEXT.find(PATTERN))

TEXT = '''Now is the time for all people to come to the aid of their party. Now is the time for all good people to
come to the aid of their party. Now is the time for many good people to come to the aid of their party.
Now is the time for all good people to come to the aid of their party. Now is the time for a lot of good
people to come to the aid of their party. Now is the time for all of the good people to come to the aid of
their party. Now is the time for all good people to come to the aid of their party. Now is the time for
each good person to come to the aid of their party. Now is the time for all good people to come to the aid
of their party. Now is the time for all good Republicans to come to the aid of their party. Now is the
time for all good people to come to the aid of their party. Now is the time for many or all good people to
come to the aid of their party. Now is the time for all good people to come to the aid of their party. Now
is the time for all good Democrats to come to the aid of their party. Now is the time for all people to
come to the aid of their party. Now is the time for all good people to come to the aid of their party. Now
is the time for many good people to come to the aid of their party. Now is the time for all good people to
come to the aid of their party. Now is the time for a lot of good people to come to the aid of their
party. Now is the time for all of the good people to come to the aid of their party. Now is the time for
all good people to come to the aid of their attack at dawn party. Now is the time for each person to come
to the aid of their party. Now is the time for all good people to come to the aid of their party. Now is
the time for all good Republicans to come to the aid of their party. Now is the time for all good people
to come to the aid of their party. Now is the time for many or all good people to come to the aid of their
party. Now is the time for all good people to come to the aid of their party. Now is the time for all good
Democrats to come to the aid of their party.'''
PATTERN = 'attack at dawn'
print(full_dfa_kmp(TEXT, PATTERN) == TEXT.find(PATTERN))

TEXT = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
PATTERN = 'aaaab'
print(full_dfa_kmp(TEXT, PATTERN) == TEXT.find(PATTERN))

TEXT = 'abcabcabc'
PATTERN = 'abcabc'
print(multi_match_kmp(TEXT, PATTERN))
