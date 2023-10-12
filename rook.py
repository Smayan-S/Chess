"""Module for rook"""
from chess_pieces import ChessPiece

class Rook(ChessPiece):
    """Class for rook"""


    def __init__(self, color, position, piece_id):
        self.has_moved = False
        super().__init__(color, position, piece_id)