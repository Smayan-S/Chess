"""Module for queen"""
from chess_pieces import ChessPiece

class Queen(ChessPiece):
    """Class for queen"""


    def __init__(self, color, position, piece_id):
        self.has_moved = False
        super().__init__(color, position, piece_id)