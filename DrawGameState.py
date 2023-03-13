import pygame
from config import Config


class DrawGameState:
    def __init__(self, screen, board):
        self.__drawBoard(screen)
        self.__drawPieces(screen, board)

    @staticmethod
    def __drawBoard(screen):
        colors = [pygame.Color("ivory"), pygame.Color("grey")]
        for row in range(Config.DIMENSION):
            for col in range(Config.DIMENSION):
                parity = (row + col) % 2
                color = colors[parity]
                square = pygame.Rect(col * Config.SQUARE_SIZE, row * Config.SQUARE_SIZE, Config.SQUARE_SIZE,
                                     Config.SQUARE_SIZE)
                pygame.draw.rect(screen, color, square)

    @staticmethod
    def __drawPieces(screen, board):
        for row in range(Config.DIMENSION):
            for col in range(Config.DIMENSION):
                piece = board[row][col]
                if piece != '--':
                    image = Config.IMAGES[piece]
                    square = pygame.Rect(col * Config.SQUARE_SIZE, row * Config.SQUARE_SIZE, Config.SQUARE_SIZE,
                                         Config.SQUARE_SIZE)
                    screen.blit(image, square)
