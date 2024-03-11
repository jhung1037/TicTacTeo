import time
import random

class Player:

    def __init__(self, sign):
        self.sign = sign
    
    def make_move(self):
        pass
    
class Human(Player):

    def __init__(self, sign):
        super().__init__(sign)
    
    def make_move(self, game):
        move = input(f"Next move for {self.sign}: ")
        while not game.valid_move(move):
            move = input(f"\033[10:1H\033[JInvalid move, try again: ")
        move = int(move)-1
        game.square_display[move] = self.sign
        game.available_squares.remove(move)
        return move

class AI(Player):
    def __init__(self, sign):
        super().__init__(sign)

    def make_move(self, game):
        move = random.choice(game.available_squares)
        game.square_display[move] = self.sign
        game.available_squares.remove(move)
        time.sleep(0.5)
        return move