"""Initializing the chess board"""
board = [['', '', '', '', '', '', '', '',],
         ['', '', '', '', '', '', '', '',],
         ['', '', '', '', '', '', '', '',],
         ['', '', '', '', '', '', '', '',],
         ['', '', '', '', '', '', '', '',],
         ['', '', '', '', '', '', '', '',],
         ['', '', '', '', '', '', '', '',],
         ['', '', '', '', '', '', '', '',]]

board[0] = ['bR','bN','bB','bQ','bK','bB','bN','bR']
board[7] = ['wR','wN','wB','wQ','wK','wB','wN','wR']
board[1] = ['bP','bP','bP','bP','bP','bP','bP','bP']
board[6] = ['wP','wP','wP','wP','wP','wP','wP','wP']

GAME_OVER = False


def update_board(source_square, target_square):
    """Update the board per move"""
    copy = board[int(source_square[0])][int(source_square[1])]
    board[int(source_square[0])][int(source_square[1])] = ''
    board[int(target_square[0])][int(target_square[1])] = copy


def find_player_pieces(value, existing_pieces):
    """Find current player pieces"""
    player_pieces = []
    if value == 1:
        for piece in existing_pieces:
            if piece[0] == 'b':
                player_pieces.append(piece)
        return player_pieces
    for piece in existing_pieces:
        if piece[0] == 'w':
            player_pieces.append(piece)
    return player_pieces


def find_on_board_pieces():
    """Finds current existing pieces"""
    existing_pieces=[]
    for rank in board:
        for pieces in rank:
            if pieces != '':
                existing_pieces.append(pieces)
    return existing_pieces


def convert_input_to_index(user_input):
    """Converts user input to indices of the chess board"""
    file_to_index = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7'}
    rank_to_index = {'1': '7', '2': '6', '3': '5', '4': '4', '5': '3', '6': '2', '7': '1', '8': '0'}

    if len(user_input) == 4:
        source_square = rank_to_index[user_input[1]] + file_to_index[user_input[0]]
        target_square = rank_to_index[user_input[3]] + file_to_index[user_input[2]]
        return source_square, target_square
    return None


def display_board():
    """Dispalys chess board"""
    rank_number = 8
    for rank in board:
        print(rank_number, end="     ")
        rank_number -= 1
        for square in rank:
            if square != '':
                print(square, end="  ")
            else:
                print(0, end="   ")
        print("\n")
    print("\n      a   b   c   d   e   f   g   h")


def simulate_game():
    """Simulates turn based chess game"""
    turn = 0
    existing_pieces = find_on_board_pieces()
    while GAME_OVER is False:
        display_board()
        if turn%2 == 0:
            moveable_pieces = find_player_pieces(0, existing_pieces)
        else:
            moveable_pieces = find_player_pieces(1, existing_pieces)
        while True:
            player_input = input()
            source_square, target_square = convert_input_to_index(player_input)
            source_square_piece = board[int(source_square[0])][int(source_square[1])]
            if source_square_piece not in moveable_pieces:
                print("Invalid piece: Enter your piece again")
                continue
            break
        update_board(source_square, target_square)
        turn += 1

simulate_game()
