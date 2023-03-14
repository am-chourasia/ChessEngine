from Move import Move
from config import Config


class ValidMovesGenerator:

    @staticmethod
    def __selectMethod(piece):
        moveFunctions = {"P": ValidMovesGenerator.getPawnMoves,
                         "R": ValidMovesGenerator.getRookMoves,
                         "N": ValidMovesGenerator.getKnightMoves,
                         "B": ValidMovesGenerator.getBishopMoves,
                         "Q": ValidMovesGenerator.getQueenMoves,
                         "K": ValidMovesGenerator.getKingMoves
                         }
        return moveFunctions[piece]

    @staticmethod
    def getValidMoves(gameState):
        return ValidMovesGenerator.getAllPossibleMoves(gameState)

    @staticmethod
    def getAllPossibleMoves(gameState) -> list:
        """
        All moves without considering check.
        """
        moves = []
        for row in range(len(gameState.board)):
            for col in range(len(gameState.board[row])):
                turn = gameState.board[row][col][0]
                if (turn == "w" and gameState.whiteToMove) or (turn == "b" and not gameState.whiteToMove):
                    piece = gameState.board[row][col][1]
                    ValidMovesGenerator.__selectMethod(piece)(row, col, moves, gameState)
        return moves

    @staticmethod
    def getPawnMoves(row, col, moves, gameState):
        if gameState.whiteToMove:  # it's white turn
            if gameState.board[row - 1][col] == '--':  # if the forward cell is empty
                moves.append(Move((row, col), (row - 1, col), gameState.board))
                # if the pawn is at the start:
                startingRow = Config.DIMENSION - 2
                if row == startingRow and gameState.board[row - 2][col] == '--':
                    moves.append(Move((row, col), (row - 2, col), gameState.board))
            # Diagonal Enemy Capture Checks:
            if col + 1 < Config.DIMENSION and gameState.board[row - 1][col + 1][0] == 'b':
                moves.append(Move((row, col), (row - 1, col + 1), gameState.board))
            if col - 1 >= 0 and gameState.board[row - 1][col - 1][0] == 'b':
                moves.append(Move((row, col), (row - 1, col - 1), gameState.board))
        else:
            if gameState.board[row + 1][col] == '--':  # if the forward cell is empty
                moves.append(Move((row, col), (row + 1, col), gameState.board))
                startingRow = 1
                if row == startingRow and gameState.board[row + 2][col] == '--':
                    moves.append(Move((row, col), (row + 2, col), gameState.board))
            if col + 1 < Config.DIMENSION and gameState.board[row + 1][col + 1][0] == 'w':
                moves.append(Move((row, col), (row + 1, col + 1), gameState.board))
            if col - 1 >= 0 and gameState.board[row + 1][col - 1][0] == 'w':
                moves.append(Move((row, col), (row + 1, col - 1), gameState.board))

    @staticmethod
    def getRookMoves(row, col, moves, gameState):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))  # up, left, down, right
        enemy_color = "b" if gameState.whiteToMove else "w"
        for direction in directions:
            for i in range(1, 8):
                end_row = row + direction[0] * i
                end_col = col + direction[1] * i
                if 0 <= end_row <= 7 and 0 <= end_col <= 7:  # check for possible moves only in boundaries of the board
                    end_piece = gameState.board[end_row][end_col]
                    if end_piece == "--":  # empty space is valid
                        moves.append(Move((row, col), (end_row, end_col), gameState.board))
                    elif end_piece[0] == enemy_color:  # capture enemy piece
                        moves.append(Move((row, col), (end_row, end_col), gameState.board))
                        break
                    else:  # friendly piece
                        break
                else:  # off board
                    break

    @staticmethod
    def getKnightMoves(row, col, moves, gameState):
        knight_moves = ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2),
                        (1, -2))  # up/left up/right right/up right/down down/left down/right left/up left/down
        ally_color = "w" if gameState.whiteToMove else "b"
        for move in knight_moves:
            end_row = row + move[0]
            end_col = col + move[1]
            if 0 <= end_row <= 7 and 0 <= end_col <= 7:
                end_piece = gameState.board[end_row][end_col]
                if end_piece[0] != ally_color:  # so its either enemy piece or empty square
                    moves.append(Move((row, col), (end_row, end_col), gameState.board))

    @staticmethod
    def getBishopMoves(row, col, moves, gameState):
        directions = ((-1, -1), (-1, 1), (1, 1), (1, -1))  # diagonals: up/left up/right down/right down/left
        enemy_color = "b" if gameState.whiteToMove else "w"
        for direction in directions:
            for i in range(1, 8):
                end_row = row + direction[0] * i
                end_col = col + direction[1] * i
                if 0 <= end_row <= 7 and 0 <= end_col <= 7:  # check if the move is on board
                    end_piece = gameState.board[end_row][end_col]
                    if end_piece == "--":  # empty space is valid
                        moves.append(Move((row, col), (end_row, end_col), gameState.board))
                    elif end_piece[0] == enemy_color:  # capture enemy piece
                        moves.append(Move((row, col), (end_row, end_col), gameState.board))
                        break
                    else:  # friendly piece
                        break
                else:  # off board
                    break

    @staticmethod
    def getKingMoves(row, col, moves, gameState):
        row_moves = (-1, -1, -1, 0, 0, 1, 1, 1)
        col_moves = (-1, 0, 1, -1, 1, -1, 0, 1)
        ally_color = "w" if gameState.whiteToMove else "b"
        for i in range(8):
            end_row = row + row_moves[i]
            end_col = col + col_moves[i]
            if 0 <= end_row <= 7 and 0 <= end_col <= 7:
                end_piece = gameState.board[end_row][end_col]
                if end_piece[0] != ally_color:  # not an ally piece - empty or enemy
                    moves.append(Move((row, col), (end_row, end_col), gameState.board))

    @staticmethod
    def getQueenMoves(row, col, moves, gameState):
        ValidMovesGenerator.getRookMoves(row, col, moves, gameState)
        ValidMovesGenerator.getBishopMoves(row, col, moves, gameState)
