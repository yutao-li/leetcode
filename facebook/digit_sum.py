def solution(digits: str, k: int) -> str:
    while len(digits) > k:
        i = 0
        compressed = ''
        while i < len(digits):
            compressed += str(sum(int(d) for d in digits[i:i + k]))
            i += k
        digits = compressed
    return digits


print(solution('13426501197', 3))
