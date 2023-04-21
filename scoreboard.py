class Scoreboard():
    def __init__(self) -> None:
        pass

    def print_scoreboard(self, score_board):
        print("\t--------------------------------")
        print("\t              SCOREBOARD       ")
        print("\t--------------------------------")

        players = list(score_board.keys())
        print("\t   ", players[0], "\t    ", score_board[players[0]])
        print("\t   ", players[1], "\t    ", score_board[players[1]])

        print("\t--------------------------------\n")
