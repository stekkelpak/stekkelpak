#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

def beats(one, two):

    # The beats function doesn't need to be defined under any class. It can be called from anywhere since it is a global function.

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Player:
    # In the Player classes, like RandomPlayer, CyclePlayer, etc. you need to define the move function that
    # defines the move of the player and the learn function that learns the opponent's last move.
    
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    def move(self):
        return random.choice(['rock', 'paper', 'scissors'])

class HumanPlayer(Player):

    """ Class whose method of movement asks the player to choose the move. """

    def __init__(self):
        super().__init__()
        self.behavior = "Human Player"


    def move(self):

        """ Method that asks the player to choose the move. """

        while True:
            move = input('What would you like to throw? (rock / paper / scissors)\n').lower()
            if move in moves:
                return move
            else:
                print("The name of the move is wrong. Try again!")


    def learn(self, my_move, their_move):
        my_move = move1
        their_move = move2

    def validate(self):



# class ReflectPlayer(Player):

#     def move(self):
#         return move(HumanPlayer)

# class CyclePlayer(Player):


class Game:

    """ Class containing the methods to initialize and process each round of the game. """
    # In the game function, you need to make functions that checks the result of the round,
    # call the round function that defines how the round is gonna played and so on...

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        move1 = self.player1.move()
        move2 = self.player2.move()
        print(f"{move1} - {move2}")
        self.player1.learn(move1, move2)
        self.player2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            # if beats == True:
            #     # https://study-hall.udacity.com/sg-613901-1967/threads/community:nd000:613901-cohort-1967-project-1956/community:thread-3433668552-235025?contextType=room
            #     print("RandomPlayer 1 wins.")
            # elif beats == False:
            #     print("RandomPlayer 2 wins.")
            # else:
            #     print("It's a tie!")
        print("Game over!")

if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()

# Here are the rules of the game: scissor cuts paper,paper covers rock, and rock crushes scissors.
# Play either "rock", "paper", or "scissors"
# If you want to stop playing, enter a "z".
# Who would you like to play with? Please enter "random", "reflect", "repeat", or "cycle"
