import pygame

GREY = (128,128,128)
WHITE = (255,255,255)
BLACK = (0,0,0)

class Board:

    def _init(self,**kwargs):
        self.width = kwargs.setdefault('width',800)
        self.height = kwargs.setdefault('height',800)
        pygame.init()
        self.win = pygame.display.set_mode((self.width,self.height))
        self.win_rect = pygame.Rect(0,0,self.width,self.height)
    
    def __init__(self,width,height):
        self._init({'width':width,'height':height})
    
    def clear(self):
        self._init()
    
    def get_game_pos(self,rows,columns):
        fl,rl = [],[]
        files = ['a','b','c','d','e','f','g','h']
        for r,c in rows,columns:
            fl.append(files[c])
            rl.append(r)
    
    def draw(self,rows,columns,square_size):
        pygame.gfxdraw.box(self.win,self.win_rect,BLACK)
        for row in range(rows+1):
            pygame.gfxdraw.hline(self.win_rect,0,self.width,row,GREY)
        for col in range(columns+1):
            pygame.gfxdraw.vline(self.win_rect,col*square_size,0,self.height,GREY)
        from game.gaming_scripts.chess.board_utils.square import Square
        rs = [i for i in range(1,rows+1)]
        cs = [i for i in range(1,columns+1)]
        squares = []
        for r in range(rows):
            for c in range(rows%2,rows,2):
                
        for _ in range(rows*columns):
            for r,c in rs,cs: