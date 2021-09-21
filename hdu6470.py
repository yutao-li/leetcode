import sys

md = 123456789
mat = [[1, 2, 1, 3, 3, 1],
       [1, 0, 0, 0, 0, 0],
       [0, 0, 1, 3, 3, 1],
       [0, 0, 0, 1, 2, 1],
       [0, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 1]]
start = [2, 1, 8, 4, 2, 1]


def tri_mat_mul(a, b):
    res = [[0] * 6 for _ in range(6)]
    for i in range(2, 6):
        res[i][i] = 1
    for i, j in [(0, 0), (1, 1), (1, 0)]:
        res[i][j] = sum(a[i][k] * b[k][j] for k in range(6)) % md
    for i in range(5):
        for j in range(i + 1, 6):
            res[i][j] = sum(a[i][k] * b[k][j] for k in range(6)) % md
    return res


def quick(num):
    if num == 2:
        return 2
    if num == 1:
        return 1
    num -= 2
    res = [[0] * 6 for _ in range(6)]
    for i in range(6):
        res[i][i] = 1
    cur = mat
    while num:
        if num & 1:
            res = tri_mat_mul(res, cur)
        cur = tri_mat_mul(cur, cur)
        num >>= 1
    return sum(i * j for i, j in zip(res[0], start)) % md


if __name__ == "__main__":
    # quick(6)
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        # 读取每一行
        num = int(sys.stdin.readline().strip())
        print(quick(num))
