"""Module containing the chess board class"""

import os
from pawn import Pawn
from knight import Knight
from bishop import Bishop
from rook import Rook
from queen import Queen 
from king import King


class ChessBoard:
    """Class containing the chess board"""


    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]

        self.board[0][0] = Rook('black', (0, 0), "bR")
        self.board[0][1] = Knight('black', (0, 1), "bN")
        self.board[0][2] = Bishop('black', (0, 2), "bB")
        self.board[0][3] = Queen('black', (0, 3), "bQ")
        self.board[0][4] = King('black', (0, 4), "bK")
        self.board[0][5] = Bishop('black', (0, 5), "bB")
        self.board[0][6] = Knight('black', (0, 6), "bN")
        self.board[0][7] = Rook('black', (0, 7), "bR")

        for col in range(8):
            self.board[1][col] = Pawn('black', (1, col), "bP")

        self.board[7][0] = Rook('white', (7, 0), "wR")
        self.board[7][1] = Knight('white', (7, 1), "wN")
        self.board[7][2] = Bishop('white', (7, 2), "wB")
        self.board[7][3] = Queen('white', (7, 3), "wQ")
        self.board[7][4] = King('white', (7, 4), "wK")
        self.board[7][5] = Bishop('white', (7, 5), "wB")
        self.board[7][6] = Knight('white', (7, 6), "wN")
        self.board[7][7] = Rook('white', (7, 7), "wR")

        for col in range(8):
            self.board[6][col] = Pawn('white', (6, col), "wP")

    def clear_terminal(self):
        """Clears the python terminal before display"""
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')


    def update_board(self, source_square, target_square):
        """Update the board per move"""
        copy = self.board[source_square[0]][source_square[1]]
        self.board[source_square[0]][source_square[1]] = None
        self.board[target_square[0]][target_square[1]] = copy


    def find_on_board_pieces(self):
        """Finds current existing pieces"""
        existing_pieces=[]
        for rank in self.board:
            for pieces in rank:
                if pieces is not None:
                    existing_pieces.append(pieces)
        return existing_pieces


    def find_player_pieces(self, color, existing_pieces):
        """Find current player pieces"""
        player_pieces = []
        if color == 'black':
            for piece in existing_pieces:
                if piece.piece_id[0] == 'b':
                    player_pieces.append(piece)
            return player_pieces
        for piece in existing_pieces:
            if piece.piece_id[0] == 'w':
                player_pieces.append(piece)
        return player_pieces


    def display_board(self):
        """Dispalys chess board"""
        self.clear_terminal()
        rank_number = 8
        print("\n\n")
        for rank in self.board:
            print(rank_number, end="     ")
            rank_number -= 1
            for square in rank:
                if square is not None:
                    print(square.piece_id, end="  ")
                else:
                    print(0, end="   ")
            print("\n")
        print("\n      a   b   c   d   e   f   g   h")
