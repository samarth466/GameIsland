import pygame


class Piece(object):

    pieces = []

    def __init__(self, image, file, rank, name, color, square_width, square_height):
        pygame.init()
        self.image_surface = pygame.image.load(image)
        self.rank = rank
        self.file = file
        self.color = color
        self.name = name
        self.square_width = square_width
        self.square_height = square_height

    def _move(self, curr_x, curr_y, delta_x, delta_y, squares, self_color, board):
        xValues = [x for x in (lambda i: i.getX()) if x != curr_x]
        yValues = [y for y in (lambda i: i.getY()) if y != curr_y]
        colors = []
        for square in squares:
            colors.append(square.color)
        if x+delta_x in xValues and y+delta_y in yValues:
            if {k: v for (k, v) in zip(zip(xValues, yValues), colors)}[(x, y)] == self_color:
                board.remove_piece(x, y)
                x += delta_x
                y += delta_y
        return (x, y)

    def _update_attacked_pieces(self, direction, curr_x, curr_y, delta_x, delta_y, square_width, square_height, squares, self_color, lower_x_bound=None, upper_x_bound=None, lower_y_bound=None, upper_y_bound=None):
        attacked_pieces = []
        xValues = [x for x in filter(lambda i: False if i.piece_x == curr_x else True, squares)]
        yValues = [y for y in filter(lambda i: False if i.piece_y == curr_y else True, squares)]
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

    def get_window_pos(self, rank=None, file=None):
        self.possible_files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        x = None
        y = None
        if rank and file:
            x = self.possible_files.index(file.lower())*100
            y = self.square_height*7-(self.rank-1)*100
        else:
            x=self.possible_files.index(self.file.lower())*100
            y=self.square_height*7-(rank-1)*100
        return (x, y)

    def get_game_pos(self, x = None, y = None):
        file=None
        rank=None
        if x and y:
            rank=x/100+1
            file=self.possible_files[(self.square_height*8-y)/100-1]
        else:
            rank=x/100+1
            file=self.possible_files[(self.square_height*8-y)/100-1]
        return (self.file, self.rank)

    def draw(self, win):
        win.blit(self.image_surface, pygame.Rect(
            0, 0, self.square_width, self.square_height))

    class Meta:
        abstract=True
