"""Module for knight"""
from chess_pieces import ChessPiece

class Knight(ChessPiece):
    """Class for knight"""


    def __init__(self, color, position, piece_id):
        self.has_moved = False
        super().__init__(color, position, piece_id)