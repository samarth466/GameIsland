import pygame
import pygame_gui

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
RED = (255, 0, 0)
SQUARE_WIDTH = 100
SQUARE_HEIGHT = 100
WIN_WIDTH = 100
WIN_HEIGHT = 800
pygame.init()
pygame.display.init()
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
MANAGER = pygame_gui.UIManager((WIN_WIDTH, WIN_HEIGHT))