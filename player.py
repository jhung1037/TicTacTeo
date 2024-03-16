import time
import random


class Player:

    def __init__(self, sign):
        self.sign = sign

    def make_move(self):
        pass


class Human(Player):

    def make_move(self, game):
        move = input(f"Next move for {self.sign}: ")
        while not game.valid_move(move):
            move = input(f"\033[10H\033[JInvalid move, try again: ")
        move = int(move)-1
        game.square_display[move] = self.sign
        game.available_squares.remove(move)
        return move


class Computer(Player):

    def make_move(self, game):
        move = random.choice(game.available_squares)
        game.square_display[move] = self.sign
        game.available_squares.remove(move)
        time.sleep(0.5)
        return move


class Computer_Easy(Computer):

    def make_move(self, game):
        move = random.choice(game.available_squares)
        game.square_display[move] = self.sign
        game.available_squares.remove(move)
        time.sleep(0.5)
        return move


class Computer_Hard(Computer):

    def make_move(self, game):
        if len(game.available_squares) == 9:
            move = random.choice([0,2,4,6,8])
            game.square_display[move] = self.sign
            game.available_squares.remove(move)
            return move
        else:
            best_move = self.minimax(game, self.sign, None)["move"]
            game.square_display[best_move] = self.sign
            game.available_squares.remove(best_move)
            time.sleep(0.5)
            return best_move

    def minimax(self, current, player, move):
        opponent = "X" if player == "O" else "O"

        if current.check_winner(opponent, move) == opponent:
            score = len(current.available_squares)+1
            return {
                "move": None,
                "score": score if opponent == self.sign else -score,
                "sum_score": score if opponent == self.sign else -score,
            }
        elif not current.available_squares:
            return {"move": None, "score": 0, "sum_score": 0}

        moves = []

        for possible_move in current.available_squares:

            current.square_display[possible_move] = player
            undo_position = current.available_squares.index(possible_move)
            current.available_squares.remove(possible_move)

            possibility = self.minimax(current, opponent, possible_move)

            current.square_display[possible_move] = " "
            current.available_squares.insert(undo_position, possible_move)
            possibility["move"] = possible_move

            moves.append(possibility)

        decision_func = max if player == self.sign else min
        best = decision_func(moves, key=lambda m: (m["score"], m["sum_score"]))
        best["sum_score"] = sum(m["score"] for m in moves)

        return best
