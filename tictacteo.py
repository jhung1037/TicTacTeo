import player

class Game:

    def __init__(self):
        self.turns = 0
        self.square_display = [" " for i in range(1,10)]
        self.available_squares = [i for i in range(9)]
    
    def print_board(self):
        print("\033[3;1H\033[J\n1 | 2 | 3\t", end = '')
        for i,s in enumerate(self.square_display):
            if i == 8:
                print(s,"\n")
            elif i == 2:
                print(s,"\n- + - + -\t- + - + -", end = '')
                print("\n4 | 5 | 6\t", end = '')
            elif i == 5:
                print(s,"\n- + - + -\t- + - + -", end = '')
                print("\n7 | 8 | 9\t", end = '')
            else:
                print(s,"|", end = ' ')

    def valid_move(self, move):
        try:
            move = int(move)
        except(ValueError):
            return False
        return move-1 in self.available_squares

    def check_winner(self, player, move):
        win_patterns = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7], [2, 4, 6], [2, 5, 8], [3, 4, 5], [6, 7, 8]]
        possible_patterns = [pattern for pattern in win_patterns if move in pattern]
        if any(all(self.square_display[i]==player.sign for i in pattern) for pattern in possible_patterns):
            self.print_board()
            print(f"{player.sign} WINS in {self.turns} turns!!!")
            exit()

    def play(self, player):
        self.print_board()
        move = player.make_move(self)
        self.turns += 1
        if self.turns >= 5:
            self.check_winner(player, move)
            if self.turns >= 9:
                self.print_board()
                print("Draw...")
                exit()


def choose_level(sign):
    cursor_row = 3 if sign == "X" else 2

    level_mapping = {"1": "easy", "2": "hard"}
    level = input("Computer level? 1.Easy 2.Hard ")

    while level not in level_mapping:
        level = input(f"\033[{cursor_row}H\033[JInvalid Selection...\nComputer level? 1.Easy 2.Hard ")
    
    cursor_row -= 1
    print(f"\033[{cursor_row}H\033J{sign} = 1.Human 2.Computer? 2.Computer({level_mapping[level]})")
    return player.Computer_Easy(sign) if level == "1" else player.Computer_Hard(sign)

def register_player(sign):
    if sign == "X":
        cursor_row = 2
        print(f"\033[{cursor_row}H\033[J", end = '')
    else:
        cursor_row = 1

    type_mapping = {"1": "1.Human", "2": "2.Computer"}
    player_type = input(f"{sign} = 1.Human 2.Computer? ")

    while player_type not in type_mapping:
        player_type = input(f"\033[{cursor_row}H\033[JRegister Failed...\n{sign} = 1.Human 2.Computer? ")

    print(f"\033[{cursor_row}H\033[J{sign} = 1.Human 2.Computer? {type_mapping[player_type]}")
    return player.Human(sign) if player_type == "1" else choose_level(sign)
    

if __name__ == "__main__":
    print("\033[H\033[J", end = '')
    game = Game()

    O = register_player("O")
    X = register_player("X")

    while True:
        game.play(O)
        game.play(X)