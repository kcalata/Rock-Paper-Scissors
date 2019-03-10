#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return random.choice(['rock', 'paper', 'scissors'])


class HumanPlayer(Player):
    def move(self):
        move = input('Rock, paper, scissors? > ').lower()
        if move == 'rock' or move == 'paper' or move == 'scissors':
            return move
        self.move()


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_move = random.choice(['rock', 'paper', 'scissors'])

    def move(self):
        return self.my_move

    def learn(self, my_move, their_move):
        self.my_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_move = random.choice(['rock', 'paper', 'scissors'])

    def move(self):
        return self.my_move

    def learn(self, my_move, their_move):
        if my_move == 'rock':
            self.my_move = 'paper'
        elif my_move == 'paper':
            self.my_move = 'scissors'
        else:
            self.my_move = 'rock'


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if self.p1.beats(move1, move2):
            print('** PLAYER ONE WINS **')
            self.p1_score += 1
        elif self.p2.beats(move2, move1):
            print('** PLAYER TWO WINS **')
            self.p2_score += 1
        else:
            print('** TIE **')
        print(f'Score: Player One {self.p1_score}, Player Two {self.p2_score}')

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        if self.p1_score > self.p2_score:
            print('** PLAYER ONE WON OVERALL **')
        elif self.p2_score > self.p1_score:
            print('** PLAYER TWO WON OVERALL **')
        else:
            print('** TIE OVERALL **')
        print(f'Final Score: Player One {self.p1_score},'
              f' Player Two {self.p2_score}')


if __name__ == '__main__':
    game = Game(HumanPlayer(), Player())
    game.play_game()
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
