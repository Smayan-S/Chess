"""Module for bishop"""
from chess_pieces import ChessPiece

class Bishop(ChessPiece):
    """Class for bishop"""


    def __init__(self, color, position, piece_id):
        self.has_moved = False
        super().__init__(color, position, piece_id)