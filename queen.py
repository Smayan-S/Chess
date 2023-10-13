"""Module for queen"""
from chess_pieces import ChessPiece

class Queen(ChessPiece):
    """Class for queen"""


    def __init__(self, color, position, piece_id):
        self.has_moved = False
        super().__init__(color, position, piece_id)

    
    def get_legal_moves(self, board):
        """Checks all legal moves of the rook"""

        legal_moves = []

        #all possible queen directions
        queen_move_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]

        #iterating through the queen directions
        for row_offset, column_offset in queen_move_directions:
            row, column = self.position
            while True:
                row += row_offset
                column += column_offset
                #checks whether the target square exists on the board
                if 0 <= row < 8 and 0 <= column < 8:
                    target_piece = board[row][column]
                    #checks whether target is empty or not
                    if target_piece is not None:
                        #makes sure the piece we capture is the opponent's piece
                        if target_piece.color is not self.color:
                            legal_moves.append((row, column))
                        #since the position is not emtpy, we must stop looking for further moves
                        break
                    #adds move if target square is empty
                    else:
                        legal_moves.append((row, column))
                else:
                    break
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
