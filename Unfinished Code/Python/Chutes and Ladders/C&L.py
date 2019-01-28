#Michael Freeman
#Chutes and Ladders
#(Insert Date completed here)

#imports
###############################################################################
import random

#global variables
###############################################################################
p1p = []
p2p = []
p3p = []
p4p = []
EMPTY = " "

#classes
###############################################################################
class Player():

    print("\nIf you're seeing this, I work!")
    def __init__(self, name, num):
        print("\nIf you're seeing this, init works!")
        self.name = name
        self.position = -1
        self.player_num = num
        #This is how you can get the initial of a player name
        self.token = self.name[0]
    def roll(self):
        die1 = random.randrange(1,6)
        die2 = random.randrange(1,6)
        roll = die1
        print("You rolled a",die1)
        return roll

    def move(self):
        print("I work!")
        roll = self.roll()
        if self.position + roll <= 99:
            oldpos = self.position
            self.position = self.position + roll
            if self.player_num == 1:
                p1p[oldpos] = EMPTY
                p1p[self.position] = self.token
            elif self.player_num == 2:
                p2p[oldpos] = EMPTY
                p2p[self.position] = self.token
            elif self.player_num == 3:
                p3p[oldpos] = EMPTY
                p3p[self.position] = self.token
            elif self.player_num == 4:
                p4p[oldpos] = EMPTY
                p4p[self.position] = self.token
        else:
            print("You need to roll a " + str(100 - self.position) + " to land exactly on 100.")

    def win(self):
        if self.position == 99:
            return self.token
        else:
            return None

class Board(object):
    pass

class Space(object):
    pass

#functions
###############################################################################
def ask_num():
    pass

def switch_turn():
    pass

def winner_grats():
    pass
#main
###############################################################################
def main():
    game = Player("Jack", 1)
    print(game.name)
    print(game.token)
    print(game.position)
    roll = game.roll()
    print(roll)
    for i in range(100):
        p1p.append(EMPTY)
    winner = None
    while not winner:
        game.move()
        winner = game.win()
        print(p1p)
        input()
    print(winner)
    print("You win!")



#run
###############################################################################
main()