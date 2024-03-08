class Game:
    
    def __init__(self):
        self.value = [i+1 for i in range(9)]
    
    def print_board(self):
        print()
        for i,v in enumerate(self.value):
            if i == 8:
                print(v,"\n")
            elif i == 2 or i == 5:
                print(v,"\n- + - + -")
            else:
                print(v,"|", end=' ')

    def check_vaild(self, move):
        while move<1 or move>9 or not isinstance(self.value[move-1], int):
            move = int(input(f"Invalid move, try again: "))
        return True

    def round(self, player):
        game.print_board()
        next_move = int(input(f"Next move for {player}: "))
        if game.check_vaild(next_move):
            game.value[next_move-1] = player

class Player:

    def __init__(self, sign):
        self.sign = sign
    

if __name__ == "__main__":
    game = Game()

    O = input("O = 1.Human 2.Computer? ")
    if O == "1" or O == "1.":
        O = Player("O")

    X = input("X = 1.Human 2.Computer? ")
    if X == "1" or X == "1.":
        X = Player("X")

    while True:
        game.round("O")
        game.round("X")


    
