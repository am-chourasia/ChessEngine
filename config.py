import pygame


class Config:
    BOARD_HEIGHT = BOARD_WIDTH = 512
    DIMENSION = 8
    SQUARE_SIZE = BOARD_HEIGHT // 8
    IMAGES = {}
    MAX_FPS = 15

    @staticmethod
    def loadImages():
        pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']
        for piece in pieces:
            Config.IMAGES[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"),
                                                        (Config.SQUARE_SIZE, Config.SQUARE_SIZE))
