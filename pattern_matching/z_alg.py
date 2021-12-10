from typing import List


def z_alg(text: str, pattern: str) -> List[int]:
    s = pattern + '$' + text
    Z = []
    for i, (a, b) in enumerate(zip(s, s[1:])):
        if a != b:
            Z.append(i)
            break
    L = 1
    R = Z[0]
    