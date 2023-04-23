class Engine():
    def __init__(self) -> None:
        self.board_values = [' ' for x in range(9)]

    def print_tic_tac_toe(self):
        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(
            self.board_values[0], self.board_values[1], self.board_values[2]))
        print('\t_____|_____|_____')

        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(
            self.board_values[3], self.board_values[4], self.board_values[5]))
        print('\t_____|_____|_____')

        print("\t     |     |")

        print("\t  {}  |  {}  |  {}".format(
            self.board_values[6], self.board_values[7], self.board_values[8]))
        print("\t     |     |")
        print("\n")

    # Function to check if any player has won
    def check_win(self, player_position, current_player):

        # All possible winning combinations
        solutions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                     [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

        # Loop to check if any winning combination is satisfied
        for solution in solutions:
            if all(item in player_position[current_player] for item in solution):
                # Return True if any winning combination satisfies
                return True
        # Return False if no combination is satisfied
        return False

    # Function to check if the game is drawn
    def check_draw(self, player_position, player_1, player_2):
        if len(player_position[player_1]) + len(player_position[player_2]) == 9:
            return True
        return False

    def single_game(self, player_1, player_2):

        # Stores the positions occupied by players
        player_position = {player_1: [], player_2: []}

        # Current player starts with the first one
        current_player = player_1

        # Game Loop for a single game of Tic Tac Toe
        while True:
            self.print_tic_tac_toe()

            # Try exception block for input
            try:
                print(
                    f"{current_player}, please choose a position in the board: ", end="")
                move = int(input())
            except ValueError:
                print(
                    "Wrong Input. It has to be a number from 1 to 9, which represents the position in the board, please try again.")
                continue

            # Sanity check for MOVE input
            if move < 1 or move > 9:
                print(
                    "Wrong position number. It has to be a number from 1 to 9, which represents the position in the board, please try again.")
                continue

            # Check if the box is not occupied already
            if self.board_values[move-1] != ' ':
                print("Position already filled, please try again.")
                continue

            # Updating grid status
            if current_player == player_1:
                self.board_values[move - 1] = 'X'
            else:
                self.board_values[move - 1] = 'O'

            # Updating player positions
            player_position[current_player].append(move)

            # Function call for checking win
            if self.check_win(player_position, current_player):
                self.print_tic_tac_toe()
                print(f"{current_player} has won this round!")
                print("\n")
                # Reset board
                self.board_values = [' ' for x in range(9)]
                return current_player

            # Function call for checking draw game
            if self.check_draw(player_position, player_1, player_2):
                self.print_tic_tac_toe()
                print("It's a draw")
                print("\n")
                # Reset board
                self.board_values = [' ' for x in range(9)]
                return 'D'

            # Switch player moves
            if current_player == player_1:
                current_player = player_2
            else:
                current_player = player_1
