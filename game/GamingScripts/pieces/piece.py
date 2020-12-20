import pygame

class Piece:

    def __init__(self, image, file, rank, name, color):
        pygame.init()
        self.image = pygame.image.load(image)
        self.rank = rank
        self.file = file
        self.color = color
        self.name = name

    def _move(self, x, y, delta_x, delta_y, squares,self_color,board):
        xValues = [x for x in filter(function=lambda i: False if i.piece_x == x else True, squares)]:
        yValues = [y for y in filter(function=lambda i: False if i.piece_y == y else True, squares)]
        colors = []
        for square in squares:
            colors.append(square.color)
        if x+delta_x in xValues and y+delta_y in yValues:
            if {k:v for (k,v) in zip(zip(xValues,yValues),colors)}[(x,y)] == self_color:
                board.remove_piece(x,y)
                x += delta_x
                y += delta_y
        return (x, y)

    def _update_attacked_pieces(self, direction, x, y, lower_x_bound=None, upper_x_bound=None, lower_y_bound=None, upper_y_bound=None, delta_x, delta_y, square_width, square_height, squares, self_color):
        attacked_pieces = []
        xValues = [x for x in filter(function=lambda i: False if i.piece_x == x else True, squares)]:
        yValues = [y for y in filter(function=lambda i: False if i.piece_y == y else True, squares)]
        colors = []
        for square in squares:
            colors.append(square.color)
        coordinates = zip(xValues, yValues, colors)
        if direction == 0 or direction == 2:
            while y >= lower_y_bound and y < upper_y_bound:
                y += square_height
                for other_x, other_y, color in coordinates:
                    if x == other_x and y == other_y:
                        if self_color != color:
                            attacked_pieces.append((x, y))
                            y -= square_height
                        else:
                            y -= square_height
                            break
        if direction == 1 or direction == 3:
            while x >= lower_x_bound and x < upper_x_bound:
                x += square_width
                for other_x, other_y, color in coordinates:
                    if x == other_x and y == other_y:
                        if self_color != color:
                            attacked_pieces.append((x, y))
                            x -= square_width
                        else:
                            x -= square_width
                            break
                    if direction == 4 or direction == 6 or direction == 5 or direction == 7:
                        while (lower_x_bound <= x < upper_x_bound) and (lower_y_bound <= y < upper_y_bound):
                            x += square_width
                y += square_height
                for other_x, other_y, color in coordinates:
                    if x == other_x and y == other_y:
                        if self_color != color:
                            attacked_pieces.append((x, y))
                            x -= square_width
                            y -= square_height
                        else:
                            x -= square_width
                            y -= square_height
                            break
        return attacked_pieces

    def get_window_pos(self,rank=None,file=None):
        self.possible_files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        x = None
        y = None
        if rank and file:
            x = (rank-1)*100
            y = self.possible_files.index(file)*100
        else:
            x = (self.rank-1)*100
            y = self.possible_files.index(self.file)*100
        return (x, y)

    def get_game_pos(self, x=None, y=None):
        self.file = None
        self.rank = None
        if not x and not y:
            self.rank = self.piece_x/100+1
            self.file = self.possible_files[self.piece_y/100]
        else:
            self.rank = x/100+1
            self.file = self.possible_files[y/100]
        return (self.file, self.rank)