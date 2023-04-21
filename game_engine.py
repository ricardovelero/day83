class Engine():
    def __init__(self) -> None:
        self.values = [' ' for x in range(9)]

    def print_tic_tac_toe(self):
        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(
            self.values[0], self.values[1], self.values[2]))
        print('\t_____|_____|_____')

        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(
            self.values[3], self.values[4], self.values[5]))
        print('\t_____|_____|_____')

        print("\t     |     |")

        print("\t  {}  |  {}  |  {}".format(
            self.values[6], self.values[7], self.values[8]))
        print("\t     |     |")
        print("\n")

    # Function to check if any player has won
    def check_win(self, player_pos, cur_player):

        # All possible winning combinations
        solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                    [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

        # Loop to check if any winning combination is satisfied
        for x in solution:
            if all(y in player_pos[cur_player] for y in x):
                # Return True if any winning combination satisfies
                return True
        # Return False if no combination is satisfied
        return False

    # Function to check if the game is drawn
    def check_draw(self, player_pos, player_1, player_2):
        if len(player_pos[player_1]) + len(player_pos[player_2]) == 9:
            return True
        return False

    def single_game(self, player_1, player_2):

        # Stores the positions occupied by players
        player_pos = {player_1: [], player_2: []}

        # Current player starts with the first one
        cur_player = player_1

        # Game Loop for a single game of Tic Tac Toe
        while True:
            self.print_tic_tac_toe()

            # Try exception block for MOVE input
            try:
                print(
                    f"{cur_player}, please choose a position in the board: ", end="")
                move = int(input())
            except ValueError:
                print(
                    "Wrong Input. It has to be a number from 1 to 9, which represents the position in the board, please try again.")
                continue

            # Sanity check for MOVE inout
            if move < 1 or move > 9:
                print(
                    "Wrong position number. It has to be a number from 1 to 9, which represents the position in the board, please try again.")
                continue

            # Check if the box is not occupied already
            if self.values[move-1] != ' ':
                print("Position already filled, please try again.")
                continue

            # Updating grid status
            if cur_player == player_1:
                self.values[move - 1] = 'X'
            else:
                self.values[move - 1] = 'O'

            # Updating player positions
            player_pos[cur_player].append(move)

            # Function call for checking win
            if self.check_win(player_pos, cur_player):
                self.print_tic_tac_toe()
                print(f"{cur_player} has won this round!")
                print("\n")
                # Reset board
                self.values = [' ' for x in range(9)]
                return cur_player

            # Function call for checking draw game
            if self.check_draw(player_pos, player_1, player_2):
                self.print_tic_tac_toe()
                print("It's a draw")
                print("\n")
                # Reset board
                self.values = [' ' for x in range(9)]
                return 'D'

            # Switch player moves
            if cur_player == player_1:
                cur_player = player_2
            else:
                cur_player = player_1
