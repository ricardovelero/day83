from game_engine import Engine
from scoreboard import Scoreboard

scoreboard = Scoreboard()
game = Engine()

if __name__ == "__main__":

    player_1 = input("Player 1, enter your name : ").title()

    player_2 = input("Player 2, enter your name : ").title()

    # Stores the scoreboard
    score_board = {player_1: 0, player_2: 0}
    scoreboard.print_scoreboard(score_board)

    # Main game Loop
    while True:

        # Stores the winner in a single game of Tic Tac Toe
        winner = game.single_game(player_1, player_2)

        # Edits the scoreboard according to the winner
        if winner != 'D':
            score_board[winner] = score_board[winner] + 1

        scoreboard.print_scoreboard(score_board)

        again = input("Do you want to play again? (Y)es or (N)o? ").upper()
        if again == 'N' or again == 'NO':
            break
