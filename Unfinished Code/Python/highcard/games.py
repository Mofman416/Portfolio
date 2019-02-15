import cards

def ask_num(ask, min, max):
    """Ask for a number in the range by checking it against a pre-set range"""
    #Asks for the number of players. This is important because it sets the amount of players in a game, and makes sure
    #the player input does not go over a specific range.
    while True:
        num = 0
        num = input(ask)
        try:
            num = int(num)
        except ValueError:
            print("Error! Cannot convert.")
        if num in range(min, max + 1):
            return num
        else:
            print("Invalid range of players.")

def switch_turn(num_players, turn):
    """Changes the turn between players by checking if the turn is less than the number of players. If so, proceed,
    otherwise return to first player."""
    #Switches the turn between players.
    turn = turn
    if turn < num_players - 1:
        turn += 1
        return turn
    else:
        turn = 0
        return turn

def winner_grats():
    """Winning message!"""
    print("\n-----------You win!------------")

def ask_permission(question):
    """Ask for permission to do anything defined in the question by passing it in from an outside function
    i.e. question = 'What's your favorite food?'
    ask_permission(question)"""
    #Asks yes or no, loops if invalid answer
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question+ "Y or N ").lower()
    return response

def roll(self):
    """Rolls the dice by choosing a random number and returning the roll."""
    #This rolls the dice.
    die1 = random.randrange(1,6)
    die2 = random.randrange(1,6)
    roll = die1
    print("You rolled a",die1)
    return roll

class Player(object):
    """A Player for the game."""
    def __init__(self, name):
        self.name = name
        self.hand = cards.Hand()
    def __str__(self):
        rep = self.name
        rep = rep+" "+str(self.hand.cards[0])
        return rep

if __name__ == "__main__":
    print("You called this module directly and didn't import it, you spoon!")
    input("\n\nPress enter to quit.")

