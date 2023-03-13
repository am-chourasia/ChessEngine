class GameState:
    def __init__(self):
        """
            Board is a 8x8 2d list, each element in list has 2 characters.
            The first character represents the color of the piece: 'b' or 'w'.
            The second character represents the type of the piece: 'R', 'N', 'B', 'Q', 'K' or 'p'.
            '--' represents an empty space with no piece.
        """
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]

        self.whiteToMove = True
        self.move_log = []

    def makeMove(self, move):
        startRow, startCol = move.start_row, move.start_col
        endRow, endCol = move.end_row, move.end_col
        self.board[startRow][startCol] = '--'           # the source of the move becomes empty
        self.board[endRow][endCol] = move.piece_moved   # the destination becomes the source piece
        self.move_log.append(move)
        self.whiteToMove = not self.whiteToMove
