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
            if col + 1 < Config.DIMENSION and gameState.board[row + 1][col + 1][0] != 'w':
                moves.append(Move((row, col), (row + 1, col + 1), gameState.board))
            if col - 1 >= 0 and gameState.board[row + 1][col - 1][0] != 'w':
                moves.append(Move((row, col), (row + 1, col - 1), gameState.board))

    @staticmethod
    def getRookMoves(row, col, moves, gameState):
        pass

    @staticmethod
    def getKnightMoves(row, col, moves, gameState):
        pass

    @staticmethod
    def getBishopMoves(row, col, moves, gameState):
        pass

    @staticmethod
    def getKingMoves(row, col, moves, gameState):
        pass

    @staticmethod
    def getQueenMoves(row, col, moves, gameState):
        pass
