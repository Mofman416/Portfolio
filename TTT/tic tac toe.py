#Michael Freeman
#12/10/18
#Let's play some Tic Tak Toe!

#global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARE = 9

#functions
def instructions():
    #Display Instructions
    print("""Welcome, player. \n""")

    print(
        """You are going to play Tick Tack Toe with me. \n
        Think you can beat me?
        You're welcome to try!

        Make your move by entering a number 0-8. The number positions
        will be like this:

                    0|1|2
                    -----
                    3|4|5
                    -----
                    6|7|8

        C'mere, punk! \n
        """
        )

def ask_permission(question):
    #Asks yes or no, loops if invalid answer
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question+ "y or n").lower()
    return response

def ask_num(question, low, high):
    #Checks to see if number is in range
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low, high):
                break
                break
            elif response not in range(low, high):
                response = input(question)
        else:
            print("Invalid, try again")
            response = input(question)
    return int(response)
        

#instructions()

#ask_permission("Do you want something to eat?")

x=ask_num("Input a number between 0 and 8 ",0, 9)
print(x)
