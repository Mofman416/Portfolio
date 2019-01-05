import sys

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

##file = open_file("test_file.txt", "w")
##file.write("this/is/a/Test")
##file.close()
##file = open_file("test_file.txt", "r")
##line = read_line(file)
##print(line)
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
    file = open_file("test.txt", "r")
    title = read_line(file)
    welcome(title)
    score = 0
    category, question, answers, correct, explanation = next_block(file)
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
        category, question, answers, correct, explanation = next_block(file)
    file.close()
    print("You've completed the quiz!\n")
    return score

##file = open_file("test_file.txt", "r")
##category, question, answers, correct, explanation = next_block(file)
##print(category)
##print(question)
##print(answers)
##print(correct)
##print(explanation)

show = main()
print(show)
