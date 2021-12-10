def boyer_moore(text: str, pattern: str) -> int:
    if len(text) < len(pattern):
        return -1
    text = [ord(i) for i in text]
    pattern = [ord(i) for i in pattern]
    right_most = [-1] * 128
    for i, ch in enumerate(pattern):
        right_most[ch] = i
    i = 0
    while i <= len(text) - len(pattern):
        skip = 0
        for j in range(len(pattern) - 1, -1, -1):
            if pattern[j] != text[i + j]:
                skip = max(1, j - right_most[text[i + j]])
        if skip == 0:
            return i
        i += skip
    return -1


PATTERN = 'NEEDLE'
TEXT = 'INAHAYSTACKNEEDLEINA'
print(boyer_moore(TEXT, PATTERN) == TEXT.find(PATTERN))

TEXT = 'ABACADABRAC'
PATTERN = 'ABRA'
print(boyer_moore(TEXT, PATTERN) == TEXT.find(PATTERN))

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
print(boyer_moore(TEXT, PATTERN) == TEXT.find(PATTERN))

TEXT = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
PATTERN = 'aaaab'
print(boyer_moore(TEXT, PATTERN) == TEXT.find(PATTERN))
