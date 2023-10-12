"""Module for the controller"""

class Controller:
    """Class to handle gui to engine interaction"""

    def __inti__(self):
        pass


    def convert_input_to_index(self, user_input):
        """Converts user input to indices of the chess board"""
        file_to_index = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                         'e': 4, 'f': 5, 'g': 6, 'h': 7}
        rank_to_index = {'1': 7, '2': 6, '3': 5, '4': 4,
                         '5': 3, '6': 2, '7': 1, '8': 0}

        if len(user_input) == 4:
            source_square = (rank_to_index[user_input[1]], file_to_index[user_input[0]])
            target_square = (rank_to_index[user_input[3]], file_to_index[user_input[2]])
            return source_square, target_square
        return None


    def validate_input_format(self, player_input):
        """Validates if input is in format letter-number-letter-number"""
        if len(player_input) != 4:
            print("Enter a valid input (E.g. e2e4)")
            return -1
        if not (player_input[0].isalpha() and player_input[2].isalpha() and
                player_input[1].isnumeric() and player_input[3].isnumeric()):
            print("Enter a valid input (E.g. e2e4)")
            return -1
        if not 'a' <= player_input[0] <= 'h':
            print("Input valid source square")
            return -1
        if not 'a' <= player_input[2] <= 'h':
            print("Input valid target square")
            return -1
        if not '1' <= player_input[1] <= '8':
            print("Input valid source square")
            return -1
        if not '1' <= player_input[3] <= '8':
            print("Input valid target square")
            return -1
        return 0