"""Module for knight"""
from chess_pieces import ChessPiece

class Knight(ChessPiece):
    """Class for knight"""


    # def __init__(self, color, position, piece_id):
    #     super().__init__(color, position, piece_id)


    def get_legal_moves(self, board):
        """Get's all legal moves for the night"""

        legal_moves = []

        #all possible knight moves
        knight_moves = [(-2, -1), (-2, 1),
                        (-1, -2), (-1, 2),
                        (1, -2), (1, 2),
                        (2, -1), (2, 1)]
        current_row, current_column = self.position
        for row_offset, column_offset in knight_moves:
            next_row = current_row + row_offset
            next_column = current_column + column_offset
            #checks whether move is within the board
            if 0 <= next_row < 8 and 0 <= next_column < 8:
                target_piece = board[next_row][next_column]
                #checks whether same color piece is not on target square
                if target_piece is not None and target_piece.color is self.color:
                    continue
                legal_moves.append((next_row, next_column))

        return legal_moves


    def move(self, target_square):
        """Updates the new position of that piece"""
        self.position = target_square


    def is_legal_move(self, target_square, board):
        """Checks whether user input is a legal mvoe"""
        legal_moves = self.get_legal_moves(board)
        if target_square not in legal_moves:
            return -1
        self.move(target_square)
        return 0
    