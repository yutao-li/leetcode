from typing import Union


def fitPuzzle(pieces: {str: [[int, int]]}, width, height):
    def flip_horizontal(grids: [[int, int]]) -> [[int, int]]:
        return [row[::-1] for row in grids]

    def flip_vertical(grids: [[int, int]]) -> [[int, int]]:
        n = len(grids)
        m = len(grids[0])
        newGrids = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                newGrids[i][j] = grids[n - 1 - i][j]
        return newGrids

    def transpose(grids: [[int, int]]) -> [[int, int]]:
        n = len(grids)
        m = len(grids[0])
        newGrids = [[0] * n for _ in range(m)]
        for j in range(m):
            for i in range(n):
                newGrids[j][i] = grids[i][j]
        return newGrids

    def transform(grids: [[int, int]]) -> [[int, int]]:
        transposeGrids = transpose(grids)
        possible = [grids, flip_horizontal(grids), flip_vertical(grids), flip_horizontal(flip_vertical(grids)),
                    transposeGrids, flip_horizontal(transposeGrids), flip_vertical(transposeGrids),
                    flip_vertical(flip_horizontal(transposeGrids))]
        newGrids = []
        for i in possible:
            if i not in newGrids:
                newGrids.append(i)
        return newGrids

    def canFit(board: [[Union[int, str]]], piece, row, column) -> bool:
        n = len(piece)
        m = len(piece[0])
        for i in range(n):
            for j in range(m):
                if piece[i][j] == 1 and board[row + i][column + j] != 0:
                    return False
        return True

    def fitPiece(board: [[Union[int, str]]], piece: [[int, int]], row: int, column: int, id: str) -> [
        [Union[int, str]]]:
        newBoard = [row[:] for row in board]
        n = len(piece)
        m = len(piece[0])
        for i in range(n):
            for j in range(m):
                if piece[i][j] == 1:
                    newBoard[row + i][column + j] = id
        return newBoard

    def printBoard(board: [[str]]):
        for row in board:
            for i in row:
                print(i, end='')
            print()
        print()

    def tryFit(board: [[Union[int, str]]], iPiece: int):
        if iPiece == numPiece:
            printBoard(board)
            return
        for piece in transformation[iPiece]:
            n = len(piece)
            m = len(piece[0])
            for i in range(height - n + 1):
                for j in range(width - m + 1):
                    if canFit(board, piece, i, j):
                        newBoard = fitPiece(board, piece, i, j, ids[iPiece])
                        tryFit(newBoard, iPiece + 1)

    numPiece = len(pieces)
    ids = list(pieces)
    transformation = [transform(piece) for piece in pieces.values()]
    if sum(sum(row) for piece in pieces.values() for row in piece) != width * height:
        return
    board = [[0] * width for _ in range(height)]
    tryFit(board, 0)


pieces = {'A': [[1, 0], [1, 0], [1, 1]], 'B': [[1, 1], [1, 1]], 'C': [[1, 1]]}
width = 2
height = 5
fitPuzzle(pieces, width, height)
