import pygame
from .CONSTANTS import (GREY,WHITE,BLACK,UPPER_OFFSET,LOWER_OFFSET,SCREEN,WIN_WIDTH,WIN_HEIGHT,SQUARE_WIDTH,SQUARE_HEIGHT)
from .player import Player
from .board import Board

def main(username1,username2,color1,color2):
    pygame.init()
    player1 = Player(color1,username1)
    player2 = Player(color2,username2)
    board = Board((WIN_WIDTH,WIN_HEIGHT),SQUARE_WIDTH,SQUARE_HEIGHT,player1,player2,SCREEN,UPPER_OFFSET,LOWER_OFFSET)
    clock = pygame.time.Clock()
    FPS = 60
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                run = False
        Board.move()
    pygame.quit()