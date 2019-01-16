#Michael Freeman
#January 2019
#4th/5th

import sys
import time

################################################################################
def open_file(file_name, mode):
    #This opens the file
    try:
        file = open(file_name, mode)
    except IOError as e:
        print("Sorry, invalid operation.\n")
        input("Press enter to quit.")
        sys.exit()
    else:
        return file
################################################################################
def read_line(file):
    #Returns the next line from the trivia file, formatted
    line = file.readline()
    line = line.replace("/", "\n")
    return line

################################################################################
def next_block(file):
    #This returns a block of data from the trivia file
    category = read_line(file)
    question = read_line(file)
    answers = []
    for i in range(4):
        answer = read_line(file)
        answers.append(answer)
    correct = read_line(file)
    if correct:
        correct = correct[0]
    explanation = read_line(file)
    return category, question, answers, correct, explanation
################################################################################
def welcome(title):
    #Welcome the player and get his/her name
    print("\t\tWelcome to Trivia Challenge!\nRead the Questions and answer correctly using\nnumbers 1-4. You have ten questions. Good luck!\n")
    print("\t\t", title, "\n")
################################################################################
def main():
    #Begins the testing
    #Calls up the file
    file = open_file("test.txt", "r")
    #Sets the title
    title = read_line(file)
    welcome(title)
    #Sets up the score
    score = 0
    category, question, answers, correct, explanation = next_block(file)
    #Display goes as long as there is something for a category.
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(i+1, answers[i])
        answer = input("Type the Correct Answer from 1-4. ")
        if answer == correct:
            print("\nGood one!\n")
            score += 1
        else:
            print("\nSorry!\n")
        print(explanation, "\n")
        print(score, "\n")
        time.sleep(5)
        category, question, answers, correct, explanation = next_block(file)
        #Close the file
    file.close()
    print("You've completed the quiz! Your final score is:\n")
    return score

#Execute the program.
show = main()
print(show)
time.sleep(100)
