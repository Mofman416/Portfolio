#Michael Freeman
#February 2019
#Python 4th/5th

import random

class Card(object):
    """A playing card###
    This class will ubild a single card
    Ti build a card call Card() and pass in a rank and a suit
    card1 = Card(rank = "A", suit = "S"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]


    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.face_up = True

    def flip(self):
        self.face_up = not self.face_up

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand(object):
    """A hand of playing cards"""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

my_hand = Hand()

your_hand = Hand()
deck = []
for i in range(10):
    card = Card(rank = random.choice(Card.RANKS), suit = random.choice(Card.SUITS))
    deck.append(card)

for i in range(5):
    my_hand.add(deck.pop())
    your_hand.add(deck.pop())
print(my_hand)
print(your_hand)

my_hand.give(my_hand.cards[0], your_hand)

print(my_hand)
print(your_hand)

my_hand.clear()
your_hand.clear()

print(my_hand)
print(your_hand)