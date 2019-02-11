#Michael Freeman
#February 2019
#Python 4th/5th


class Card(object):
    """A playing card
    This class will build a single card
    To build a card call Card() and pass in a rank and a suit
    card1 = Card(rank = "A", suit = "S"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♧", "♦", "♥", "♤"]


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

class Deck(Hand):
    """This will give cards to a hand, shuffle them, or deal them out.
    To make  a hand call Deck and pass in a variable for the hand
    To shuffle use your new deck and use .shuffle()
    to deal them out using deck.deal(x) with X being the amount of cards in a new hand."""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Positionable_Card(rank,suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)

                else:
                    print("Can't continue to deal. Out of cards!")


class Unprintable_Card(Card):
    """A Card that won't reveal its rank or suit when presented"""
    def __str__(self):
        return "<unprintable>"

class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up= False):
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep
    def flip(self):
        self.is_face_up = not self.is_face_up



def main():
    """Deals cards and shows them.
    First you need to create the overall deck by using populate and shuffle
    then you need to create a hand function by passing it into Hand, then making an
    empty hand list, then appending hand1 to said list.
    Then you deal from deck using deal from hands for 5 cards, then print.
    Repeat for the number of players.
    Then use a for loop in the range of the length of the hand of cards,
    use flip in the cards list in each index.
    Repeat for the amount of players."""
    deck = Deck()
    deck.populate()
    deck.shuffle()
    print(deck)

    hand1 = Hand()
    hands = []
    hands.append(hand1)
    deck.deal(hands, 5)
    print("\n",hand1)

    hand2 = Hand()
    hands = []
    hands.append(hand2)
    deck.deal(hands, 5)
    print("\n",hand2)

    for i in range(len(hand1.cards)):
        hand1.cards[i].flip()
    print("\n", hand1)

    for i in range(len(hand2.cards)):
        hand2.cards[i].flip()
    print("\n", hand2)


main()