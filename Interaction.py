from Move import Move


class Interaction:
    def __init__(self):
        self.square_selected = ()  # keeps track of the last click of the user
        self.player_clicks = []  # keeps the latest two clicks

    def reset(self):
        self.__init__()

    '''
        Returns true if the move was made with the interaction, otherwise false
    '''
    def click(self, row, col, gameState, validMoves) -> bool:
        if self.square_selected == (row, col):  # user clicked the same square twice
            self.reset()
        else:
            square_selected = (row, col)
            self.player_clicks.append(square_selected)  # append for both 1st and 2nd click

        if len(self.player_clicks) == 2:  # a move is made:
            move = Move(self.player_clicks[0], self.player_clicks[1], gameState.board)
            if move in validMoves:
                gameState.makeMove(move)
                self.reset()
                return True

        return False
