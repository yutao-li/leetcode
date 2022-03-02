class Connect6:
    def __init__(self, size: int):
        self.size = size
        self.pieces = dict()
        self.turn = 0

    def take(self, row: int, col: int):
        if not (0 <= row < self.size and 0 <= col < self.size):
            raise ValueError('Invalid coordinate.')
        if (row, col) in self.pieces:
            raise ValueError('Already taken.')
        self.pieces[row, col] = self.turn
        if self.win(row, col):
            print(str(self.turn) + ' wins.')
        self.turn = int(not self.turn)

    def win(self, row: int, col: int) -> bool:
        def streak(row, col, x_shift, y_shift) -> int:
            count = 0
            while 0 <= x_shift + row < self.size and 0 <= y_shift + col < self.size and self.pieces.get(
                    (x_shift + row, y_shift + col), -1) == self.turn:
                count += 1
                row += x_shift
                col += y_shift
            return count

        directions = [[1, 0], [0, 1], [-1, 1], [1, 1]]
        for x, y in directions:
            if streak(row, col, x, y) + streak(row, col, -x, -y) == 5:
                return True
        return False


connect6 = Connect6(10)
for i in range(6):
    connect6.take(i, i)
    connect6.take(i, 9 - i)
