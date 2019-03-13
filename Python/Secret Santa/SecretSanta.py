#Michael Freeman

import sys
import random

names = []


class Santa:
    def __init__(self, names):
        self.turns = names
        self.people = []
        for name in self.turns:
            self.people.append(name)
        self.final = []

    def sort_names(self):
        self.final = []
        self.people = []
        for name in self.turns:
            self.people.append(name)
        random.shuffle(self.people)
        for name in self.turns:
            pair = [name, random.choice(self.people)]
            if pair[0] == pair[1]:
                pair = (name, random.choice(self.people))
            self.final.append(pair)
            self.people.remove(pair[1])

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
        name = input("\nInput a name or press enter to scramble. ")
        if name.upper() == "":
            break
        else:
            names.insert(0, name)

    print(names)
    start = Santa(names)

    while True:
        start.sort_names()
        start.print_name()
        choice = input("\nDo you want to scramble again? ")
        if choice.upper() == "N":
            break
    input("Press enter to close the program. ")
    sys.exit()


main()
