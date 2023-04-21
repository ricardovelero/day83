from game_engine import Engine
from scoreboard import Scoreboard

scoreboard = Scoreboard()
game = Engine()

if __name__ == "__main__":

    player_1 = input("Player 1, enter your name : ")

    player_2 = input("Player 2, enter your name : ")

    # Stores the player who chooses X and O
    cur_player = player_1

    # Stores the choice of players
    player_choice = {'X': "", 'O': ""}

    # Stores the options
    options = ['X', 'O']

    # Stores the scoreboard
    score_board = {player_1: 0, player_2: 0}
    scoreboard.print_scoreboard(score_board)

    # Main game Loop
    while True:
        print(f"{cur_player}, please choose:")
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")

        # Try exception for CHOICE input
        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue

        # Conditions for player choice
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player_1:
                player_choice['O'] = player_2
            else:
                player_choice['O'] = player_1

        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player_1:
                player_choice['X'] = player_2
            else:
                player_choice['X'] = player_1

        elif choice == 3:
            print("Final Scores")
            scoreboard.print_scoreboard(score_board)
            break

        else:
            print("Wrong Choice!!!! Try Again\n")
            continue

        # Stores the winner in a single game of Tic Tac Toe
        winner = game.single_game(options[choice-1])

        # Edits the scoreboard according to the winner
        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        scoreboard.print_scoreboard(score_board)
        # Switch player who chooses X or O
        if cur_player == player_1:
            cur_player = player_2
        else:
            cur_player = player_1
