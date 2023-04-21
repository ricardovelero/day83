def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


def player_move(player):
    print(f"{player}, your move:")
    player_move = input("Enter your move position: ")

    if player_move == 'Q' or player_move == 'q':
        global is_game_on
        is_game_on = False
        return is_game_on
    else:
        player_move = int(player_move)
        if values[player_move - 1] != 'X' or values[player_move - 1] != 'O':
            if player == player_1:
                values[player_move - 1] = 'X'
            else:
                values[player_move - 1] = 'O'
        else:
            print("Wrong move, try again")


values = [' ' for x in range(9)]
scores = {}

print("Player 1\n")
player_1 = input("Please enter your name: ").title()
print("\n")

print("Player 2\n")
player_2 = input("Please enter your name: ").title()
print("\n")

scores[player_1] = 0
scores[player_2] = 0

is_game_on = True
while is_game_on:
    print_tic_tac_toe(values)

    player_move(player_1)

    print_tic_tac_toe(values)

    player_move(player_2)
