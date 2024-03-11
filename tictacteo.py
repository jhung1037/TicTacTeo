import time
import random


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

class Player:

    def __init__(self, sign):
        self.sign = sign
    
    def make_move(self, game):
        move = input(f"Next move for {self.sign}: ")
        while not game.valid_move(move):
            move = input(f"\033[10:1H\033[JInvalid move, try again: ")
        move = int(move)-1
        game.square_display[move] = self.sign
        game.available_squares.remove(move)
        return move

class AI:
    def __init__(self, sign):
        self.sign = sign

    def make_move(self, game):
        move = random.choice(game.available_squares)
        game.square_display[move] = self.sign
        game.available_squares.remove(move)
        time.sleep(0.5)
        # print(f"{self.sign} takes square {move+1}")
        return move

if __name__ == "__main__":
    print("\033[H\033[J", end = '')
    game = Game()


    O = input("O = 1.Human 2.AI? ")
    while True:
        if O == "1" or O == "1." or O.upper() == "HUMAN" or O.upper() == "1.HUMAN":
            print("\033[H\033[JO = 1.Human 2.AI? 1.Human")
            O = Player("O")
            break
        elif O == "2" or O == "2." or O.upper() == "AI"  or O.upper() == "2.AI":
            print("\033[H\033[JO = 1.Human 2.AI? 2.AI")
            O = AI("O")
            break
        O = input("\033[H\033[JRegister Failed...\nO = 1.Human 2.AI? ")

    X = input("X = 1.Human 2.AI? ")
    while True:
        if X == "1" or X == "1." or X.upper() == "HUMAN" or X.upper() == "1.HUMAN":
            print("\033[2;1H\033[JO = 1.Human 2.AI? 1.Human")
            X = Player("X")
            break
        elif X == "2" or X == "2." or X.upper() == "AI"  or X.upper() == "2.AI":
            print("\033[2;1H\033[JO = 1.Human 2.AI? 2.AI")
            X = AI("X")
            break
        X = input("\033[2;1H\033[JRegister Failed...\nX = 1.Human 2.AI? ")
    # O = AI("O")
    # X = AI("X")
    while True:
        game.play(O)
        game.play(X)