def solution(numbers: [[int]]) -> [[int]]:
    def beauty(col: int) -> int:
        nums = numbers[0][2 * col:2 * col + 2] + numbers[1][2 * col:2 * col + 2]
        if 1 not in nums:
            return 1
        if 2 not in nums:
            return 2
        if 3 not in nums:
            return 3
        if 4 not in nums:
            return 4
        return 5

    cols = len(numbers[0]) // 2
    beauties = sorted((beauty(i), i) for i in range(cols))
    return [[j for _, i in beauties for j in numbers[0][2 * i:2 * i + 2]],
            [j for _, i in beauties for j in numbers[1][2 * i:2 * i + 2]]]


numbers = [[1, 2, 2, 3, 2, 10, 1, 2], [3, 4, 10, 2, 5, 4, 4, 1]]
print(solution(numbers))
