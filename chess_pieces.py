"""Module for all chess pieces"""

class ChessPiece:
    """Class containing common piece information"""

    def __init__(self, color, position, piece_id):
        self.color = color
        self.position = position
        self.has_moved = False
        self.piece_id = piece_id


    def get_legal_moves(self, board):
        """Get's all legal moves (to be overriden)"""


    def is_legal_move(self, target_square, board):
        """Checks whether input is a legal move or not"""


    def move(self, target_square):
        """Moves the piece to the new position"""
