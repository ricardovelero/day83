from game_engine import Engine
from scoreboard import Scoreboard

scoreboard = Scoreboard()
game = Engine()

if __name__ == "__main__":

    player_1 = input("Player 1, enter your name : ")

    player_2 = input("Player 2, enter your name : ")

    # Stores the choice of players
    players = {'X': player_1, 'O': player_2}

    # Stores the scoreboard
    score_board = {player_1: 0, player_2: 0}
    scoreboard.print_scoreboard(score_board)

    # Main game Loop
    while True:

        # Stores the winner in a single game of Tic Tac Toe
        winner = game.single_game(player_1, player_2)

        # Edits the scoreboard according to the winner
        if winner != 'D':
            player_won = players[winner]
            score_board[player_won] = score_board[player_won] + 1

        scoreboard.print_scoreboard(score_board)

        again = input("Do you want to play again? (Y)es or (N)o?").upper()
        if again == 'N' or again == 'NO':
            break
