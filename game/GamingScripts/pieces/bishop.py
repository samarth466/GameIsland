import pygame
from game.gaming_scripts.pieces.piece import Piece

class Bishop(Piece):

    def __init__(self,image,file,rank,color,min_x,max_x,min_y,max_y,square_width,square_height,win_width,win_height):
        pygame.init()
        self.image = image
        self.image_surface = pygame.image.load(image)
        self.rank = rank
        self.file = file
        self.color = color
        self.name = 'Bishop'
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.square_width = square_width
        self.square_height = square_height
        self.win_width = win_width
        self.win_height = win_height
        self.piece_x,self.piece_y = pygame.mouse.get_pos()
        self.x,self.y = self.piece_x,self.piece_y
        self.attacked_pieces = []
        self.has_moved = False
        super().__init__(self.image,self.file,self.rank,self.name,self.color)
    
    def move(self,squares,win):
        if not isinstance(squares,list):
            raise TypeError('The squares attribute must be a list.')
        limiting_pos = [[self.min_x,self.max_x],[self.min_y,self.max_y]]
        pieces = []
        max_length = 1
        selected = False
        direction = 0
        max_direction = 4
        direction_offset = 4
        pygame.font.init()
        while (self.x in limiting_pos[0] and self.y in limiting_pos[1]):
            if len(pieces) > max_length:
                fnt = pygame.font.SysFont("comicsans",40)
                txt = fnt.render("You can't select that piece because you have already selected a piece. You must either move the already selected piece or unselect it.")
                win.blit(txt,(self.max_x-(txt.get_width/2)/2,self.max_y-(txt.get_height()/2)/2))
            self.file,self.rank = self.get_game_pos()
            for event in pygame.event.get():
                if event.type == pygame.K_SPACE or event.type == pygame.K_RETURN:
                    if (self.x,self.y,self.name) in pieces:
                        selected = False
                        pieces.pop()
                    else:
                        selected = True
                        pieces.append((self.x,self.y,self.name))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_KP1] or keys[pygame.K_1] and not (keys[pygame.K_KP1] and keys[pygame.K_1]):
                self.x,self.y = self._move(self.x,self.y,-self.square_width,-self.square_height,squares)
                self.piece_x = self.x
                self.piece_y = self.y
                self.has_moved = True
            if keys[pygame.K_KP3] or keys[pygame.K_3] and not (keys[pygame.K_KP3] and keys[pygame.K_3]):
                self.x,self.y = self._move(self.x,self.y,self.square_width,self.square_height,squares)
                self.piece_x = self.x
                self.piece_y = self.y
                self.has_moved = True
            if keys[pygame.K_KP7] or keys[pygame.K_7] and not (keys[pygame.K_KP7] and keys[K_7]):
                self.x,self.y = self._move(self.x,self.y,-self.square_width,-self.square_height,squares)
                self.piece_x = self.x
                self.piece_y = self.y
                self.has_moved = True
            if keys[pygame.K_KP9] or keys[pygame.K_9] and not (keys[pygame.K_KP9] and keys[pygame.K_9]):
                self.x,self.y = self._move(self.x,self.y,self.square_width,-self.square_height,squares)
                self.piece_x = self.x
                self.piece_y = self.y
                self.has_moved = True
            while direction < max_direction:
                if direction == 0:
                        self.attacked_pieces = self._update_attacked_pieces(direction+direction_offset,self.x,self.y,lower_x_bound=0,upper_x_bound=self.win_width,lower_y_bound=0,upper_y_bound=self.win_height,-self.square_width,-square_height,self.square_width,self.square_height,squares,self.color)
                    if direction == 1:
                        self.attacked_pieces = self._update_attacked_pieces(direction+direction_offset,self.x,self.y,lower_x_bound=0,upper_x_bound=self.win_width,lower_y_bound=0,upper_y_bound=self.win_height,-self.square_width,0,square_width,square_height,squares,self.color)
                    if direction == 2:
                        self.attacked_pieces = self._update_attacked_pieces(direction+direction_offset,self.x,self.y,lower_x_bound=0,upper_x_bound=self.win_width,lower_y_bound=0,upper_y_bound=self.win_height,0,self.square_height,self.square_width,self.square_height,squares,self.color)
                    if direction == 3:
                        self.attacked_pieces = self._update_attacked_pieces(direction+direction_offset,self.x,self.y,lower_x_bound=0,upper_x_bound=self.win_width,lower_y_bound=0,upper_y_bound=self.win_height,self.square_width,0,square_width,self.square_height,squares,self.color)
                    direction += 1
            direction = 0
        self.x,self.y = self.piece_x,self.piece_y
        return self.attacked_pieces