"""Module is the main engine for the chess game"""
from chess_board import ChessBoard
from controller import Controller

cb = ChessBoard()
cn = Controller()
GAME_OVER = False


def simulate_game():
    """Simulates turn based chess game"""
    turn = 0
    while GAME_OVER is False:
        existing_pieces = cb.find_on_board_pieces()
        cb.display_board()
        if turn%2 == 0:
            moveable_pieces = cb.find_player_pieces('white', existing_pieces)
        else:
            moveable_pieces = cb.find_player_pieces('black', existing_pieces)
        while True:
            player_input = input()
            validity = cn.validate_input_format(player_input)
            if validity == -1:
                continue
            source_square, target_square = cn.convert_input_to_index(player_input)
            source_square_piece = cb.board[source_square[0]][source_square[1]]
            if source_square_piece not in moveable_pieces:
                print("Invalid piece: Enter a piece from your color again")
                continue

            if source_square_piece.is_legal_move(target_square, cb.board) != 0:
                print("Illegal move, try again")
                continue
            break
        cb.update_board(source_square, target_square)
        turn += 1

simulate_game()
