#Michael Freeman
#12/10/18
#Let's play some Tic Tak Toe!

#global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

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
        response = input(question+ "Y or N ").lower()
    return response

def ask_num(question, low, high):
    #Checks to see if number is in range
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low, high):
                break
            elif response not in range(low, high):
                response = input(question)
        else:
            print("Invalid, try again")
            response = input(question)
    return int(response)

def pieces():
    #Here we assign who goes first and assign which one goes to X or O
    go_first = ask_permission("Do you want to go first? ")
    if go_first == "y":
        print("I think I'll let you get a head start.\n")
        human = X
        computer = O
    else:
        print("You must be very brave or quite incompetent!\n")
        human = O
        computer = X
    return human, computer

def new_board():
    #This is the new board to make.
    board = []
    for squares in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    #This disaplys the board on the screen.
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\n\t", board[6], "|", board[7], "|", board[8])

def legal_moves(board):
    #Creates a list of legal moves
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    #This function defines winning conditions
    WAYS_TO_WIN = ((0,1,2),
            (3,4,5),
            (6,7,8),
            (0,3,6),
            (1,4,7),
            (2,5,8),
            (0,4,8),
            (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

        if EMPTY in board:
            return TIE
        
        return None
        

