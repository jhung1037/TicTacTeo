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


class Player:

    def __init__(self, sign):
        self.sign = sign
    
    def play(self, game):
        move = int(input(f"Next move for {self.sign}: "))
        while move<1 or move>9 or not isinstance(game.value[move-1], int):
            move = int(input(f"Invalid move, try again: "))
        game.value[move-1] = self.sign
        return move
    

if __name__ == "__main__":
    game = Game()

    O = input("O = 1.Human 2.Computer? ")
    if O == "1" or O == "1.":
        O = Player("O")

    X = input("X = 1.Human 2.Computer? ")
    if X == "1" or X == "1.":
        X = Player("X")

    while True:
        game.print_board()
        next_move = O.play(game)
        game.print_board()
        next_move = X.play(game)


    
