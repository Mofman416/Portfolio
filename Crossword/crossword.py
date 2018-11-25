# Michael Freeman & Parker Gowans
#November 16th 2018
#4/5 Period

import time

#This is the Puzzle string.
puzzle = "ofunctionypwnoynjrzwehaziigydxriepnrnjtzallatpipbcteotedrzwi"+"opoagbtfqfrpboeasidysvrlrinputdnmflppmcn"

#This displays the puzzle in rows as a function.
def display_puzzle():
    print("Row 0:", puzzle[0:10])
    print("Row 1:", puzzle[10:20])
    print("Row 2:", puzzle[20:30])
    print("Row 3:", puzzle[30:40])
    print("Row 4:", puzzle[40:50])
    print("Row 5:", puzzle[50:60])
    print("Row 6:", puzzle[60:70])
    print("Row 7:", puzzle[70:80])
    print("Row 8:", puzzle[80:90])
    print("Row 9:", puzzle[90:])
    print()

# These are the variables that the function uses.
total = 0
point = 20
earn = point
attempts = 0
pointred = 0

##Function looks good, update questions and finish programs.##

#This function checks to see if the input is in range.
def foundWord(iNum, wordToFind):
    global point
    global earn
    global attempts
    global pointred
    global total
    toReturn=0
    if len(iNum) != len(wordToFind)*2:
        return "Invalid input! Out of Range!"
    iWord = ""    
    i=0
    while i < len(wordToFind)*2:
        z = i + 2
        index=iNum[i:z] #get next two numbers
        index = int(index)
        iWord=iWord+puzzle[index]
        i+=2
    print()
    print("You've tried to find 'input'...")
    print()
    #time.sleep(2)
    print(iWord)
    print()
    if iWord == wordToFind:
        print("You were correct!")
        print()
        toReturn=1
    else:
        print("That's incorrect! Try again.")
        print()
        attempts += 1
        print("That's", attempts, "attempts.")
        
    return toReturn


#This is the word length keys.

word1_length=len("input")
word2_length=len("function")
word3_length=len("print")
word4_length=len("integer")
word5_length=len("string")
word6_length=len("operators")
word7_length=len("boolean")
word8_length=len("if")
word9_length=len("while")
word10_length=len("float")

total = 0
point = 20
earn = point
attempts = 0
pointred = 0
    
#This is the crossword game
def crossword():
    #initialize the score keeping
    global point
    global earn
    global attempts
    global pointred
    global total
    
    #Question 1
    
    x=0
    while x==0:
        ans = input("Question 1: What is used to get user defined values in a variable? (Contrast Output) ")
        print()
        if ans.lower() == "input":
            total += earn
            foundword=""
            earn = point
            pointred = 0
            x=1
        elif ans.lower() == "show":
            print(total)
            print()
        else:
            print("Try again.")
            attempts += 1
            print("That's", attempts, " attempts.")
            if pointred <= 5:
                earn = point/2
                pointred += 1
    #Puzzle 1
    x=0
    while x==0:
        print("Good Job! Now enter the index positions of 'input' in this puzzle: ")
        print()
        display_puzzle()
        f=0
        while f==0:
            print()
            inputNumbers = input("Enter the index positions of 'input'. ")
            if inputNumbers.isdigit():
                seekWordLength=word1_length
                inputLetters=""
                f = foundWord(inputNumbers,'input')                
            else:
                print()
                print("Please input a valid response. No letters or decimals please.")
                print()                
                
        break            


    #Question 2
    
    x=0
    while x==0:
        ans = input("Question 2: What do programmers use to 'package' code? (Rhymes with Junction) ")
        print()
        if ans.lower() == "function":
            total += earn
            foundword=""
            earn = point
            pointred = 0
            x=1
        elif ans.lower() == "show":
            print(total)
            print()
        else:
            print("Try again.")
            attempts += 1
            print("That's", attempts, " attempts.")
            if pointred <= 5:
                earn = point/2
                pointred += 1
    #Puzzle 2
    x=0
    while x==0:
        print("Good Job! Now enter the index positions of 'function' in this puzzle: ")
        print()
        display_puzzle()
        f=0
        while f==0:
            print()
            inputNumbers = input("Enter the index positions of 'function'. ")
            if inputNumbers.isdigit():
                seekWordLength=word2_length
                inputLetters=""
                f = foundWord(inputNumbers,'function')                
            else:
                print()
                print("Please input a valid response. No letters or decimals please.")
                print()                
                
        break            

    #Question 3
    
    x=0
    while x==0:
        ans = input("Question 3: What is used to display output to the user? (It's in Sprint.) ")
        print()
        if ans.lower() == "print":
            total += earn
            foundword=""
            earn = point
            pointred = 0
            x=1
        elif ans.lower() == "show":
            print(total)
            print()
        else:
            print("Try again.")
            attempts += 1
            print("That's", attempts, " attempts.")
            if pointred <= 5:
                earn = point/2
                pointred += 1
    #Puzzle 3
    x=0
    while x==0:
        print("Good Job! Now enter the index positions of 'print' in this puzzle: ")
        print()
        display_puzzle()
        f=0
        while f==0:
            print()
            inputNumbers = input("Enter the index positions of 'print'. ")
            if inputNumbers.isdigit():
                seekWordLength=word3_length
                inputLetters=""
                f = foundWord(inputNumbers,'print')                
            else:
                print()
                print("Please input a valid response. No letters or decimals please.")
                print()                
                
        break            

    #Question 4
    
    x=0
    while x==0:
        ans = input("Question 4: What is a whole number and isn't a decimal? (Regetni) ")
        print()
        if ans.lower() == "integer":
            total += earn
            foundword=""
            earn = point
            pointred = 0
            x=1
        elif ans.lower() == "show":
            print(total)
            print()
        else:
            print("Try again.")
            attempts += 1
            print("That's", attempts, " attempts.")
            if pointred <= 5:
                earn = point/2
                pointred += 1
    #Puzzle 4
    x=0
    while x==0:
        print("Good Job! Now enter the index positions of 'integer' in this puzzle: ")
        print()
        display_puzzle()
        f=0
        while f==0:
            print()
            inputNumbers = input("Enter the index positions of 'integer'. ")
            if inputNumbers.isdigit():
                seekWordLength=word4_length
                inputLetters=""
                f = foundWord(inputNumbers,'integer')                
            else:
                print()
                print("Please input a valid response. No letters or decimals please.")
                print()                
                
        break

    #Question 5
    
    x=0
    while x==0:
        ans = input("Question 5: What is a series of characters in code? (Most sweaters are made with ______.) ")
        print()
        if ans.lower() == "string":
            total += earn
            foundword=""
            earn = point
            pointred = 0
            x=1
        elif ans.lower() == "show":
            print(total)
            print()
        else:
            print("Try again.")
            attempts += 1
            print("That's", attempts, " attempts.")
            if pointred <= 5:
                earn = point/2
                pointred += 1
    #Puzzle 5
    x=0
    while x==0:
        print("Good Job! Now enter the index positions of 'string' in this puzzle: ")
        print()
        display_puzzle()
        f=0
        while f==0:
            print()
            inputNumbers = input("Enter the index positions of 'string'. ")
            if inputNumbers.isdigit():
                seekWordLength=word5_length
                inputLetters=""
                f = foundWord(inputNumbers,'string')                
            else:
                print()
                print("Please input a valid response. No letters or decimals please.")
                print()                
                
        break            

    #Question 6
    
    x=0
    while x==0:
        ans = input("Question 6: What is used to begin a math formula in code? (_p_r_t_rs) ")
        print()
        if ans.lower() == "operators":
            total += earn
            foundword=""
            earn = point
            pointred = 0
            x=1
        elif ans.lower() == "show":
            print(total)
            print()
        else:
            print("Try again.")
            attempts += 1
            print("That's", attempts, " attempts.")
            if pointred <= 5:
                earn = point/2
                pointred += 1
    #Puzzle 6
    x=0
    while x==0:
        print("Good Job! Now enter the index positions of 'operators' in this puzzle: ")
        print()
        display_puzzle()
        f=0
        while f==0:
            print()
            inputNumbers = input("Enter the index positions of 'operators'. ")
            if inputNumbers.isdigit():
                seekWordLength=word6_length
                inputLetters=""
                f = foundWord(inputNumbers,'operators')                
            else:
                print()
                print("Please input a valid response. No letters or decimals please.")
                print()                
                
        break            

    #Question 7
    
    x=0
    while x==0:
        ans = input("Question 7: What is used check values in a string? (Boo!) ")
        print()
        if ans.lower() == "boolean":
            total += earn
            foundword=""
            earn = point
            pointred = 0
            x=1
        elif ans.lower() == "show":
            print(total)
            print()
        else:
            print("Try again.")
            attempts += 1
            print("That's", attempts, " attempts.")
            if pointred <= 5:
                earn = point/2
                pointred += 1
    #Puzzle 7
    x=0
    while x==0:
        print("Good Job! Now enter the index positions of 'boolean' in this puzzle: ")
        print()
        display_puzzle()
        f=0
        while f==0:
            print()
            inputNumbers = input("Enter the index positions of 'boolean'. ")
            if inputNumbers.isdigit():
                seekWordLength=word7_length
                inputLetters=""
                f = foundWord(inputNumbers,'boolean')                
            else:
                print()
                print("Please input a valid response. No letters or decimals please.")
                print()                
                
        break            

    #Question 8
    
    x=0
    while x==0:
        ans = input("Question 8: What is used to tell the program what to do with data? (__/else statement) ")
        print()
        if ans.lower() == "if":
            total += earn
            foundword=""
            earn = point
            pointred = 0
            x=1
        elif ans.lower() == "show":
            print(total)
            print()
        else:
            print("Try again.")
            attempts += 1
            print("That's", attempts, " attempts.")
            if pointred <= 5:
                earn = point/2
                pointred += 1
    #Puzzle 8
    x=0
    while x==0:
        print("Good Job! Now enter the index positions of 'if' in this puzzle: ")
        print()
        display_puzzle()
        f=0
        while f==0:
            print()
            inputNumbers = input("Enter the index positions of 'if'. ")
            if inputNumbers.isdigit():
                seekWordLength=word8_length
                inputLetters=""
                f = foundWord(inputNumbers,'if')                
            else:
                print()
                print("Please input a valid response. No letters or decimals please.")
                print()                
                
        break            

    #Question 9
    
    x=0
    while x==0:
        ans = input("Question 9: What is used to make a loop for a specific variable? (W_ile) ")
        print()
        if ans.lower() == "while":
            total += earn
            foundword=""
            earn = point
            pointred = 0
            x=1
        elif ans.lower() == "show":
            print(total)
            print()
        else:
            print("Try again.")
            attempts += 1
            print("That's", attempts, " attempts.")
            if pointred <= 5:
                earn = point/2
                pointred += 1
    #Puzzle 9
    x=0
    while x==0:
        print("Good Job! Now enter the index positions of 'while' in this puzzle: ")
        print()
        display_puzzle()
        f=0
        while f==0:
            print()
            inputNumbers = input("Enter the index positions of 'while'. ")
            if inputNumbers.isdigit():
                seekWordLength=word9_length
                inputLetters=""
                f = foundWord(inputNumbers,'while')                
            else:
                print()
                print("Please input a valid response. No letters or decimals please.")
                print()                
                
        break            

    #Question 10
    
    x=0
    while x==0:
        ans = input("Question 10: What is a decimal called? (You _____ in space due to zero gravity.) ")
        print()
        if ans.lower() == "float":
            total += earn
            foundword=""
            earn = point
            pointred = 0
            x=1
        elif ans.lower() == "show":
            print(total)
            print()
        else:
            print("Try again.")
            attempts += 1
            print("That's", attempts, " attempts.")
            if pointred <= 5:
                earn = point/2
                pointred += 1
    #Puzzle 10
    x=0
    while x==0:
        print("Good Job! Now enter the index positions of 'float' in this puzzle: ")
        print()
        display_puzzle()
        f=0
        while f==0:
            print()
            inputNumbers = input("Enter the index positions of 'float'. ")
            if inputNumbers.isdigit():
                seekWordLength=word1_length
                inputLetters=""
                f = foundWord(inputNumbers,'float')                
            else:
                print()
                print("Please input a valid response. No letters or decimals please.")
                print()                
                
        break            

#This is how the game opens.
def menu():
    print("Welcome to the crossword game!")
    print()

    ans = input("Would you like to play? Y/N You may also type 'Quit' if you want to quit. ")
    print()

    while True:
        if ans.upper() == "Y" or ans.lower() == "yes":
            print("You will be asked a trivia question which will proceed to a crossword puzzle if answered correctly.")
            print()
        
            print("You can earn at most 20 points. Everytime you answer incorrectly half the points will be taken from you until you guess incorrectly 5 times.")
            print()

            print("Go for the perfect 200 points!!")
            print()

            print("The crossword puzzle takes two digit numbers. If you want to put in a letter from the top row be sure to include the 0 (i.e. a letter on the top row three spaces to the right would be 02).")
            print()

            print("Ready? Here we go!")
            print()
            time.sleep(5)
            crossword()
            print("Congratulations! You got", total, "out of 200 points with", attempts, "incorrect guesses!\n")
            ans = input("Want to play again (Y/N) or 'Quit'? ")
            print()
        elif ans.upper() == "N" or ans.lower() == "no":
            print("You're missing out on the game of the year 2018")
            print()
            time.sleep(1)
            menu()
        elif ans.lower() == "quit":
            print("See ya later!")
            time.sleep(3)
            exit()
        else:
            print("Invalid input, go home.")
            menu()
            
menu()

