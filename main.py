import sys
import pygame
import pygame.mouse

from DrawGameState import DrawGameState
from Interaction import Interaction
from GameState import GameState
from config import Config
from ValidMovesGenerator import ValidMovesGenerator


def main():
    pygame.init()
    pygame.display.set_caption('Chess')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((Config.BOARD_HEIGHT, Config.BOARD_WIDTH))
    screen.fill(pygame.Color("white"))
    gameState = GameState()
    Config.loadImages()

    running = True
    interaction = Interaction()
    validMoves = ValidMovesGenerator.getValidMoves(gameState)
    moveMade = False
    DrawGameState(screen, gameState.board)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // Config.SQUARE_SIZE
                row = location[1] // Config.SQUARE_SIZE
                moveMade = interaction.click(row, col, gameState, validMoves)
                print(moveMade)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                gameState.undoMove()
                moveMade = True

        if moveMade:
            validMoves = ValidMovesGenerator.getValidMoves(gameState)
            moveMade = False
            DrawGameState(screen, gameState.board)  # draw the new state of the game on the screen
        clock.tick(Config.MAX_FPS)
        pygame.display.flip()  # update the new screen on the display board


if __name__ == '__main__':
    main()
