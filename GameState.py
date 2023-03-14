from Move import Move

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

    def undoMove(self):
        if len(self.move_log) != 0:
            lastMove = self.move_log.pop()
            self.board[lastMove.start_row][lastMove.start_col] = lastMove.piece_moved
            self.board[lastMove.end_row][lastMove.end_col] = lastMove.piece_captured
            self.whiteToMove = not self.whiteToMove  # swap players

    def getValidMoves(self):
        return self.getAllPossibleMoves()

    def getAllPossibleMoves(self):
        """
        All moves without considering check.
        """
        moves = [Move((6, 4), (4, 4), self.board)]
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                turn = self.board[row][col][0]
                if (turn == "w" and self.whiteToMove) or (turn == "b" and not self.whiteToMove):
                    piece = self.board[row][col][1]
                    if piece == 'P':
                        self.getPawnMoves()
                    elif piece == 'R':
                        self.getRookMoves()
        return moves

    def getPawnMoves(self):
        pass

    def getRookMoves(self):
        pass

