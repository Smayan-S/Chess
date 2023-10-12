"""Module for the pawn piece"""
from chess_pieces import ChessPiece

class Pawn(ChessPiece):
    """Class for the pawn piece"""


    def __init__(self, color, position, piece_id):
        super().__init__(color, position, piece_id)
        self.has_moved = False
        self.move_direction = -1 if self.color == 'white' else 1


    def get_legal_moves(self, board):
        legal_moves = []
        current_row, current_column = self.position
        single_movement = False

        #for single movement
        next_row = current_row + self.move_direction
        if 0 <= next_row < 8 and board[next_row][current_column] is None:
            single_movement = True
            legal_moves.append((next_row, current_column))

        #for double movement
        if single_movement:
            if not self.has_moved:
                next_row = current_row + 2 * self.move_direction
                if board[next_row][current_column] is None:
                    legal_moves.append((next_row, current_column))

        #for captures
        column_offset = [-1, 1]
        for offset in column_offset:
            next_row = current_row + self.move_direction
            next_column = current_column + offset
            if 0 <= next_column < 8 and 0 <= next_column < 8:
                target_piece = board[next_row][next_column]
                if target_piece is not None and target_piece.color is not self.color:
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
        self.has_moved = True
        return 0
    