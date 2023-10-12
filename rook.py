"""Module for rook"""
from chess_pieces import ChessPiece

class Rook(ChessPiece):
    """Class for rook"""


    def __init__(self, color, position, piece_id):
        self.has_moved = False
        super().__init__(color, position, piece_id)


    def get_legal_moves(self, board):
        """Checks all legal moves of the rook"""

        legal_moves = []

        current_row, current_column = self.position
        up = down = left = right = True
        scale = 1

        while True:

            if up:
                up_offset = -1 * scale
                if current_row + up_offset >= 0:
                    target_piece = board[current_row + up_offset][current_column]
                    if target_piece is None:
                        legal_moves.append((current_row + up_offset, current_column))
                    else:
                        up = False
                        if target_piece.color is not self.color:
                            legal_moves.append((current_row + up_offset, current_column))
                else:
                    up = False

            if down:
                down_offset = 1 * scale
                if current_row + down_offset < 8:
                    target_piece = board[current_row + down_offset][current_column]
                    if target_piece is None:
                        legal_moves.append((current_row + down_offset, current_column))
                    else:
                        down = False
                        if target_piece.color is not self.color:
                            legal_moves.append((current_row + down_offset, current_column))
                else:
                    down = False

            if left:
                left_offset = -1 * scale
                if current_column + left_offset >= 0:
                    target_piece = board[current_row][current_column + left_offset]
                    if target_piece is None:
                        legal_moves.append((current_row, current_column + left_offset))
                    else:
                        left = False
                        if target_piece.color is not self.color:
                            legal_moves.append((current_row + left_offset, current_column))
                else:
                    left = False

            if right:
                right_offset = 1 * scale
                if current_column + right_offset < 8:
                    target_piece = board[current_row][current_column + right_offset]
                    if target_piece is None:
                        legal_moves.append((current_row, current_column + right_offset))
                    else:
                        right = False
                        if target_piece.color is not self.color:
                            legal_moves.append((current_row, current_column + right_offset))
                else:
                    right = False

            if up is down is left is right is False:
                break

            scale += 1
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
                        