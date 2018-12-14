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
###############################################################################

def ask_permission(question):
    #Asks yes or no, loops if invalid answer
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question+ "Y or N ").lower()
    return response
###############################################################################


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
###############################################################################


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
###############################################################################


def new_board():
    #This is the new board to make.
    board = []
    for squares in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
###############################################################################


def display_board(board):
    #This disaplys the board on the screen.
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\n\t", board[6], "|", board[7], "|", board[8])
###############################################################################


def legal_moves(board):
    #Creates a list of legal moves
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
###############################################################################


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
###############################################################################


def human_move(board):
    #Gets the human move
    op = legal_moves(board)
    move = None
    while move not in op:
        set_move = ask_num("Pick a spot from 0-8: ", 0, NUM_SQUARES)
        print(type(move))
        if move not in op:
            print(type(move))
            print("That's not a valid space, dummy!")
    print("Kerchoo")
    return move
###############################################################################


def next_turn(turn):
    #Switch turns
    if turn == X:
        return O
    else:
        return X
###############################################################################

def congrat_winner(winner, computer, human):
    #Congratulate the player.
    if winner != TIE:
        print(winner, "is victorious!\n")
    else:
        print("It's a tie!\n")
        if winner == computer:
            print("Gotcha punk!\n")
        elif winner == human:
            print("You win. Cool.\n")
        elif winner == TIE:
            print("A strange game. The only winning move is not to play.\n")
###############################################################################

def computer_move(board, computer, human):
    #Make a computer move.
    #make a copy to work with since function will change the list
    board = board[:]
    #the best positions to have, in order
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print("I shall take square number", end=" ")

    #if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #done checking this move, undo it
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return none
        #done check this move, undo it
        board[move] = EMPTY

    #since no one can win on next move, pick best open square.
        for move in BEST_MOVES:
            if move in legal_moves(board):
                print(move)
                return move

def main():
    display_instruction()
    pieces()
    
##board = new_board()
##print(board)
##x = legal_moves(board)
##print(x)
##move = human_move(board)

##board = new_board()
##board[4] = O
##board[0] = O
##h=X
##c=O
##move = computer_move(board, c,h)
##print(move)

human, computer = pieces()
