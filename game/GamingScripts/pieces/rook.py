import pygame
from game.gaming_scripts.pieces.piece import Piece

class Rook(Piece):

    def __init__(self,image,file,rank,color,min_x,max_x,min_y,max_y,square_width,square_height,win_width,win_height):
        pygame.init()
        self.image = image
        self.image_surface = pygame.image.load(image)
        self.rank = rank
        self.file = file
        self.color = color
        self.name = 'Rook'
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.square_width = square_width
        self.square_height = square_height
        self.win_width = win_width
        self.win_height = win_height
        self.piece_x,self.piece_y = pygame.mouse.get_pos
        self.x,self.y = self.piece_x,self.piece_y
        self.attacked_pieces = []
        self.has_moved = False
        super().__init__(self.image,self.file,self.rank,self.name,self.color)
    
    def move(self,squares,win,board):
        if not isinstance(squares,list):
            raise TypeError('The squares attribute must be a list(), not '+str(type(squares))[8:-1].capitalize()+'().')
        limiting_pos = [[self.min_x,self.max_x],[self.min_y,self.max_y]]
        max_length = 1
        selected = False
        direction = 0
        max_direction = 4
        direction_offset = 0
        pygame.font.init()
        while (self.x in limiting_pos[0] and self.y in limiting_pos[1]):
            if len(self.pieces) > max_length:
                fnt = pygame.font.SysFont("comicsans",40)
                txt = fnt.render("You can't select that piece because you have already selected a piece. You must either move the already selected piece or unselect it.")
                win.blit(txt,(self.max_x-(txt.get_width/2)/2,(self.x,self.y))
            self.file,self.rank = self.get_game_pos()
            for event in pygame.event.get():
                if event.type == pygame.K_SPACE or event.type == pygame.K_RETURN:
                    if (self.x,self.y,self.name) in pieces:
                        selected = False
                        self.pieces.pop()
                    else:
                        selected = True
                        self.pieces.append((self.x,self.y,self.name))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_KP2] or keys[pygame.K_2]:
                _,self.y = self._move(self.x,self.y,0,self.square_height,squares)
                self.piece_y = self.y
                self.has_moved = True
            if keys[pygame.K_KP4] or keys[pygame.K_4]:
                self.x,_ = self._move(self.x,self.y,-self.square_width,0,squares)
                self.piece_x = self.x
                self.has_moved = True
            if keys[pygame.K_KP6] or keys[pygame.K_6]:
                self.x,_ = self._move(self.x,self.y,self.square_width,0,squares)
                self.piece_x = self.x
                self.has_moved = True
            if keys[pygame.K_KP8] or keys[pygame.K_8]:
                _,self.y = self._move(self.x,self.y,0,-self.square_height,squares)
                self.piece_y = self.y
                self.has_moved = True
            while direction < max_direction:
                if direction == 0:
                        self.attacked_pieces = self._update_attacked_pieces(direction+direction_offset,self.x,self.y,lower_y_bound=0,upper_y_bound=self.win_height,0,-square_height,self.square_width,self.square_height,squares,self.color)
                    if direction == 1:
                        self.attacked_pieces = self._update_attacked_pieces(direction+direction_offset,self.x,self.y,lower_x_bound=0,upper_x_bound=self.win_width,-self.square_width,0,square_width,square_height,squares,self.color)
                    if direction == 2:
                        self.attacked_pieces = self._update_attacked_pieces(direction+direction_offset,self.x,self.y,lower_y_bound=0,upper_y_bound=self.win_height,0,self.square_height,self.square_width,self.square_height,squares,self.color)
                    if direction == 3:
                        self.attacked_pieces = self._update_attacked_pieces(direction+direction_offset,self.x,self.y,lower_x_bound=0,upper_x_bound=self.win_width,self.square_width,0,square_width,self.square_height,squares,self.color)
                    direction += 1
            direction = 0
        self.x,self.y = self.piece_x,self.piece_y
        return self.attacked_pieces