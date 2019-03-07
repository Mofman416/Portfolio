#Michael Freeman

import sys
import random

names = []

class Santa:
    def __init__(self, name):
        self.turns = name
        self.people = names
        self.final = []

    def sort_names(self):
        random.shuffle(self.people)
        for name in self.turns:
            pair = (name, random.choice(self.people))
            if pair[0] == [1]:
                pair = (name, random.choice(self.people))

            else:
                self.final.append(pair)

    def print_name(self):
        input("\nNames are ready! Press Enter to show the names.")
        print(self.final)

def main():
    name = input("\nType in your name. ")
    names.append(name)
    name = input("\nType in the next name. ")
    names.append(name)
    name = input("\nType in the next name. ")
    names.append(name)
    while True:
        next = input("\nIs this everyone? Y/N ")
        if next.upper() == "Y":
            break
        elif next.upper() == "N":
            name = input("\nType in the next name. ")
            names.insert(0, name)
        else:
            print("\nInvalid response, please try again.")
    print(names)
    start = Santa(names)
    start.sort_names()
    start.print_name()
    input("\nRecord these, and press enter to quit.")
    sys.exit()

main()