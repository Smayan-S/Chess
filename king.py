"""Module for king"""
from chess_pieces import ChessPiece

class King(ChessPiece):
    """Class for king"""


    def __init__(self, color, position, piece_id):
        self.has_moved = False
        super().__init__(color, position, piece_id)