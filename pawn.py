"""Module for the pawn piece"""
from chess_pieces import ChessPiece

class Pawn(ChessPiece):
    """Class for the pawn piece"""


    def __init__(self, color, position, piece_id):
        super().__init__(color, position, piece_id)
        self.has_moved = False
        self.move_direction = -1 if self.color == 'white' else 1


    def get_legal_moves(self, board):
        """Get's all possible legal moves"""

        legal_moves = []
        if self.color == 'white':
            
            #checks whether the square ahead of it is empty
            if board[self.position[0] - 1][self.position[1]] is None:
                #checks whether two squares ahead is empty or not
                if board[self.position[0] - 2][self.position[1]] is None:
                    #if pawn has not moved, it can jump two squares for it's first move
                    if self.has_moved is False:
                        legal_moves.append((self.position[0] - 2, self.position[1]))
                legal_moves.append((self.position[0] - 1, self.position[1]))

            #checks whether diagonal captures are within the limits of the board
            if (self.position[1] - 1) >= 0 and (self.position[1] + 1) <=7:
                top_left_white = board[self.position[0] - 1][self.position[1] - 1]
                top_right_white = board[self.position[0] - 1][self.position[1] + 1]
                #checks whether the left diagonal square has a piece for white
                if top_left_white is not None:
                    #makes sure the piece is not from the same color
                    if top_left_white.color is not self.color:
                        legal_moves.append((self.position[0] - 1, self.position[1] - 1))
                #checks whether the right diagonal square has a piece for white
                if top_right_white is not None:
                    #makes sure the piece is not from the same color
                    if top_right_white.color is not self.color:
                        legal_moves.append((self.position[0] - 1, self.position[1] + 1))

        elif self.color == 'black':

            #checks whether the square ahead of it is empty
            if board[self.position[0] + 1][self.position[1]] is None:
                #checks whether two squares ahead is empty or not
                if board[self.position[0] + 2][self.position[1]] is None:
                    #if pawn has not moved, it can jump two squares for it's first move
                    if self.has_moved is False:
                        legal_moves.append((self.position[0] + 2, self.position[1]))
                legal_moves.append((self.position[0] + 1, self.position[1]))


            #checks whether diagonal captures are within the limits of the board
            if (self.position[1] - 1) >= 0 and (self.position[1] + 1) <=7:
                top_right_black = board[self.position[0] + 1][self.position[1] - 1]
                top_left_black = board[self.position[0] + 1][self.position[1] + 1]
                #checks whether the right diagonal square has a piece for white
                if top_right_black is not None:
                    #makes sure the piece is not from the same color
                    if top_right_black.color is not self.color:
                        legal_moves.append((self.position[0] + 1, self.position[1] - 1))
                #checks whether the left diagonal square has a piece for white
                if top_left_black is not None:
                    #makes sure the piece is not from the same color
                    if top_left_black.color is not self.color:
                        legal_moves.append((self.position[0] + 1, self.position[1] + 1))

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
    