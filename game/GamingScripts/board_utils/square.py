import pygame

class Square(object):

    def __init__(self,rank,file,color,piece,square_width,square_height,is_empty=False):
        pygame.init()
        self.rank = rank
        self.file = file
        self.color = color
        self.is_empty = is_empty
        self.piece = piece
        self.square_width = square_width
        self.square_height = square_height
        self.is_attacked = False
    
    def get_window_pos(self):
        possible_files = ['a','b','c','d','e','f','g','h']
        x = possible_files.index(self.file.lower())*100
        y = self.square_height*7-(self.rank-1)*100
        return (x,y)
    
    def draw(self,win):
        x,y = self.get_window_pos()
        self.rect = pygame.Rect(x,y,self.square_width,self.square_height)
        self.draw_square = pygame.gfxdraw.rectangle(win,self.rect,self.color)
        self.piece.draw(self.draw_square)
        return self.draw_square
    
    def getX(self):
        return self.get_window_pos()[0]
    
    def getY(self):
        return self.get_window_pos()[1]