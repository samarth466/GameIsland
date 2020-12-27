from ..board_utils.square import Square
from ..chess.CONSTANTS import (WHITE, BLACK)
squares = [[[Square(rank, file, color, None, 100, 100, True) for rank in range(1, 8)]
            for file in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']] for color in (WHITE, BLACK)]