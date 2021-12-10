PRIME = 997
BASE = 128


def rabin_carp(text: str, pattern: str) -> int:
    if len(text) < len(pattern):
        return -1
    fingerprint = 0
    text = [ord(i) for i in text]
    pattern = [ord(i) for i in pattern]
    for i in pattern:
        fingerprint = (fingerprint * BASE + i) % PRIME
    f = 0
    R = BASE ** (len(pattern) - 1) % PRIME
    for i in text[:len(pattern)]:
        f = (f * BASE + i) % PRIME
    if f == fingerprint:
        return 0
    for i, (start, end) in enumerate(zip(text, text[len(pattern):]), 1):
        f = ((f - start * R) * BASE + end) % PRIME
        if f == fingerprint and text[i:i + len(pattern)] == pattern:
            return i
    return -1


PATTERN = 'NEEDLE'
TEXT = 'INAHAYSTACKNEEDLEINA'
print(rabin_carp(TEXT, PATTERN) == TEXT.find(PATTERN))

TEXT = 'ABACADABRAC'
PATTERN = 'ABRA'
print(rabin_carp(TEXT, PATTERN) == TEXT.find(PATTERN))

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
print(rabin_carp(TEXT, PATTERN) == TEXT.find(PATTERN))

TEXT = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
PATTERN = 'aaaab'
print(rabin_carp(TEXT, PATTERN) == TEXT.find(PATTERN))
