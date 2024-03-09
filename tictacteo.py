class Game:
    
    def __init__(self):
        self.value = [i+1 for i in range(9)]
        self.turns = 0
    
    def print_board(self):
        print()
        for i,v in enumerate(self.value):
            if i == 8:
                print(v,"\n")
            elif i == 2 or i == 5:
                print(v,"\n- + - + -")
            else:
                print(v,"|", end=' ')

    def valid_move(self, move):
        try:
            move = int(move)
        except(ValueError):
            return False
        return move>=1 and move<=9 and isinstance(self.value[move-1], int)

    def check_winner(self, player, move):
        win_patterns = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7], [2, 4, 6], [2, 5, 8], [3, 4, 5], [6, 7, 8]]
        possible_patterns = [pattern for pattern in win_patterns if move in pattern]
        for pattern in possible_patterns:
            if all(self.value[i]==player.sign for i in pattern):
                self.print_board()
                print(f"{player.sign} WINS in {self.turns} turns!!!")
                exit()

    def play(self, player):
        self.print_board()
        move = player.make_move(self)
        self.turns += 1
        if self.turns >= 5:
            if self.turns >= 9:
                self.print_board()
                print("Draw...")
                exit()
            self.check_winner(player, move)

class Player:

    def __init__(self, sign):
        self.sign = sign
    
    def make_move(self, game):
        move = input(f"Next move for {self.sign}: ")
        while not game.valid_move(move):
            move = input(f"Invalid move, try again: ")
        game.value[int(move)-1] = self.sign
        return int(move)-1

if __name__ == "__main__":
    game = Game()

    O = input("O = 1.Human 2.Computer? ")
    if O == "1" or O == "1.":
        O = Player("O")

    X = input("X = 1.Human 2.Computer? ")
    if X == "1" or X == "1.":
        X = Player("X")

    while True:
        game.play(O)
        game.play(X)